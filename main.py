import asyncio
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Form
from loguru import logger

from config import config
import opsgenie
import prtg

THRESHOLD = config['main'].getint('threshold')
NOTIFICATION_ID = config['main']['notification_id']

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

@app.get('/increment')
async def increment(date_time: str):
    '''\f
        For testing counter
    '''
    parsed_datetime = datetime.strptime(date_time, '%m/%d/%Y %I:%M:%S %p')
    count = await ingest_counter.increment(parsed_datetime)
    # find delay between alert time and the time counted
    delay = (datetime.utcnow() - parsed_datetime).total_seconds()
    logger.info(f'Count: {count} | Delay: {delay}')
    is_paused = False
    paused = False
    if count >= THRESHOLD:
        if prtg.get_notification_status(NOTIFICATION_ID):
            prtg.pause_notification(NOTIFICATION_ID)
            # build and send Opsgenie alert
            message = f'[Alert-Counter] PRTG Alert Threshold Exceeded (count: {THRESHOLD}). \
                Notification template with ID {NOTIFICATION_ID} paused.'
            description = 'Alert-Counter counts the number of alerts from PRTG and will pause \
                a configured notification template after a threshold (number of alerts per second) is met.'
            opsgenie.send_alert(message, description=description, tags=['jle-dev', 'PRTG', 'Alert-Counter'])
            paused = True
        is_paused = True
    return {
        'count': count,
        'threshold_reached': is_paused,
        'paused': paused,
        'delay': delay
    }

@app.post('/log')
async def create_log(device: str = Form(...),
                linkdevice: str = Form(...),
                sitename: str = Form(...),
                serviceurl: Optional[str] = Form(None),
                settings: str = Form(...),
                date_time: str = Form(..., alias='datetime'),
                history: Optional[str] = Form(None),
                host: str = Form(...),
                down: Optional[str] = Form(None),
                downtime: str = Form(...),
                lastdown: str = Form(...),
                nodename: Optional[str] = Form(None),
                location: Optional[str] = Form(None),
                group: str = Form(...),
                linkgroup: str = Form(...),
                lastmessage: str = Form(...),
                lastup: str = Form(...),
                uptime: str = Form(...),
                status: str = Form(...),
                statesince: str = Form(...),
                sensor: str = Form(...),
                linksensor: str = Form(...),
                probe: str = Form(...),
                priority: str = Form(...),
                commentssensor: Optional[str] = Form(None),
                commentsdevice: Optional[str] = Form(None),
                commentsgroup: Optional[str] = Form(None),
                commentsprobe: Optional[str] = Form(None),
                colorofstate: Optional[str] = Form(None),
                iconofstate: Optional[str] = Form(None),
                sensor_id: str = Form(..., alias='id')) -> dict:
    parsed_datetime = datetime.strptime(date_time, '%m/%d/%Y %I:%M:%S %p')
    count = await ingest_counter.increment(parsed_datetime)
    # find delay between alert time and the time counted
    delay = (datetime.utcnow() - parsed_datetime).total_seconds()
    logger.info(f'Count: {count} | Delay: {delay}s')
    is_paused = False
    paused = False
    if count >= THRESHOLD:
        if prtg.get_notification_status(NOTIFICATION_ID):
            prtg.pause_notification(NOTIFICATION_ID)
            # build and send Opsgenie alert
            message = f'[Alert-Counter] PRTG Alert Threshold Exceeded (count: {THRESHOLD}). \
                Notification template with ID {NOTIFICATION_ID} paused.'
            description = 'Alert-Counter counts the number of alerts from PRTG and will pause \
                a configured notification template after a threshold (number of alerts per second) is met.'
            opsgenie.send_alert(message, description=description, tags=['jle-dev', 'PRTG', 'Alert-Counter'])
            paused = True
        is_paused = True
    return {
        'count': count,
        'threshold_reached': is_paused,
        'paused': paused,
        'delay': delay
    }
