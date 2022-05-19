import xml.etree.ElementTree as ET

import requests

from config import config

USERNAME = config['prtg']['username']
PASSHASH = config['prtg']['passhash']
BASE_URL = config['prtg']['base_url']

def get_notification_status(notification_id):
    '''Check status of notification template.
    Args:
        notification_id (str): ID of notification template on PRTG. This can be found
            by going to 'Setup > Account Settings > Notification Templates', select the
            notification template, and view the 'id' parameter in the URL
    Returns:
        int: 0 for 'Paused', 1 for 'Started'
        None: if notification template cannot be found
    '''
    url = BASE_URL + '/api/getobjectproperty.htm'
    params = {
        'username': USERNAME,
        'passhash': PASSHASH,
        'id': notification_id,
        'name': 'active'
    }
    response = requests.get(url, params)
    response.raise_for_status
    root = ET.fromstring(response.text)
    result = root.find('result')
    if result is not None:
        return int(result.text)

def _pause_notification_api(notification_id, action):
    '''API to pause or resume a notification template.
    Args:
        notification_id (str): ID of notification template on PRTG. This can be found
            by going to 'Setup > Account Settings > Notification Templates', select the
            notification template, and view the 'id' parameter in the URL
        action (int): 0 to pause, 1 to resume
    Returns:
        XML response from PRTG (currently garbage; useless information is returned)
    '''
    url = BASE_URL + '/api/pause.htm'
    params = {
        'username': USERNAME,
        'passhash': PASSHASH,
        'id': notification_id,
        'action': action
    }
    response = requests.get(url, params)
    response.raise_for_status()
    return response.text

def pause_notification(notification_id):
    return _pause_notification_api(notification_id, 0)

def resume_notification(notification_id):
    return _pause_notification_api(notification_id, 1)
