import argparse
import time
from datetime import datetime

import requests

PRTG_TIME_FORMAT = '%m/%d/%Y %I:%M:%S %p'

parser = argparse.ArgumentParser(
        prog='test',
        description='Test increment endpoint')
parser.add_argument('load', type=int, default=1, help='number of times to send the request')
parser.add_argument('-m', '--modulo', type=int, help='test that increment resets after MODULO requests')

def test_increment():
    url = 'http://localhost:8000/increment'
    params = {
        'date_time': datetime.utcnow().strftime(PRTG_TIME_FORMAT)
    }

    response = requests.get(url, params)
    return response.json()

def main():
    args = parser.parse_args()
    if args.modulo:
        for i in range(1, args.load + 1):
            if i%args.modulo == 0:
                time.sleep(1)
            payload = test_increment()
            try:
                delay = payload['delay'] - last_delay
            except:
                delay = 0
            last_delay = payload['delay']
            payload['delay'] = delay
            print(payload)
    else:
        for i in range(1, args.load + 1):
            payload = test_increment()
            try:
                delay = payload['delay'] - last_delay
            except:
                delay = 0
            last_delay = payload['delay']
            payload['delay'] = delay
            print(payload)

if __name__ == '__main__':
    main()