import asyncio
import logging
import logging.handlers
import sys
from datetime import datetime

from fastapi import FastAPI, Request
from logstash import LogstashHandler
from loguru import logger

from config import config
import opsgenie
import prtg

LOG_LEVEL = config['main']['log_level'].upper()
SYSLOG = config['main'].getboolean('syslog')
SYSLOG_HOST = config['main']['sys_log_host']
SYSLOG_PORT = config['main'].getint('sys_log_port')
LOGSTASH_HOST = config['logstash']['host']
LOGSTASH_PORT = config['logstash'].getint('port')
THRESHOLD = config['main'].getint('threshold')
NOTIFICATION_ID = config['main']['notification_id']

# configure logs and syslog
if LOG_LEVEL != 'QUIET':
    if SYSLOG:
        logger.add(logging.handlers.SysLogHandler(address = (SYSLOG_HOST, SYSLOG_PORT)), level=LOG_LEVEL)

# configure logstash
logstash_logger = logging.getLogger('prtg-alert')
logstash_logger.setLevel(logging.INFO)
logstash_logger.addHandler(LogstashHandler(LOGSTASH_HOST, LOGSTASH_PORT))

with logger.catch():
    app = FastAPI()
counter_lock = asyncio.Lock()

class Counter:
    def __init__(self):
        self._count = 0
        self.date_time = None

    async def increment(self, date_time):
        try:
            if (date_time - self.date_time).total_seconds() >= 1:
                await self._reset(date_time)
        except TypeError:
            self.date_time = date_time
        async with counter_lock:
            self._count += 1
            return self._count

    async def _reset(self, date_time):
        async with counter_lock:
            self.date_time = date_time
            self._count = 0

ingest_counter = Counter()

@app.post('/log')
async def log(request: Request) -> dict:
    form_data = await request.form()
    parsed_datetime = datetime.strptime(form_data['datetime'], '%m/%d/%Y %I:%M:%S %p')
    count = await ingest_counter.increment(parsed_datetime)
    # find delay between alert time and the time counted
    delay = (datetime.utcnow() - parsed_datetime).total_seconds()
    logger.info(f'Count: {count} | Delay: {delay}s')
    logger.info(f'{form_data["group"]}/{form_data["device"]}/{form_data["sensor"]} - {form_data["lastmessage"]}')
    if count >= THRESHOLD:
        logger.warning('Threshold reached!')
        if prtg.get_notification_status(NOTIFICATION_ID):
            logger.info('Notification template is not paused.')
            logger.info('Pausing notification template...')
            prtg.pause_notification(NOTIFICATION_ID)
            logger.info(f'Notification template with ID {NOTIFICATION_ID} has been paused.')
            # build and send Opsgenie alert
            message = f'[Alert-Counter] PRTG Alert Threshold Exceeded (count: {THRESHOLD}). \
                Notification template with ID {NOTIFICATION_ID} paused.'
            description = 'Alert-Counter counts the number of alerts from PRTG and will pause \
                a configured notification template after a threshold (number of alerts per second) is met.'
            logger.info('Sending Opsgenie alert...')
            response = opsgenie.send_alert(message, description=description, tags=['jle-dev', 'PRTG', 'Alert-Counter'])
            logger.info('Opsgenie alert sent.')
            logger.debug(response)
            
    # log to logstash
    logstash_logger.info(form_data['lastmessage'], extra=form_data)
