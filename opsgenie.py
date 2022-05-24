from typing import Dict, List

import requests

from config import config

API_KEY = config['opsgenie']['api_key']
BASE_URL = config['opsgenie']['base_url']

def send_alert(message: str,
            alias: str = None, 
            description: str = None,
            responders: List[Dict[str, str]] = None,
            visibility: List[Dict[str, str]] = None,
            actions: List[str] = None,
            tags: List[str] = None,
            details: Dict[str, str] = None,
            entity: str = None,
            source: str = None,
            priority: str = None,
            user: str = None,
            note: str = None):
    url = BASE_URL + '/alerts'
    headers = {'Authorization': f'GenieKey {API_KEY}'}
    body = {
        'message': message,
        'alias': alias,
        'description': description,
        'responders': responders,
        'visibleTo': visibility,
        'actions': actions,
        'tags': tags,
        'detais': details,
        'entity': entity,
        'source': source,
        'priority': priority,
        'user': user,
        'note': note
    }
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()