import requests
import datetime
from time import sleep
import json
import yaml

with open('config.yaml', 'r') as c:
    config = yaml.safe_load(c)
key = open(config['api_key']).read()
api = 'https://api.monkeytype.com'

time = config['time']

def get_pb():
    endpoint = f'{api}/users/personalBests'
    query = {
    "mode": "time",
    "mode2":"60"
    }
    apekey = f'ApeKey {key}'
    x = requests.get(endpoint, headers={'Authorization':apekey, 'Accept':'application/json'}, \
                     allow_redirects=True, params=query)
    response = x.json()
    pb = response['data'][0]['wpm']
    return pb

def changeLine(n, text):
    with open(config['out_file'], 'r', encoding='utf-8') as f:
        data = f.readlines()
    data[n] = text
    with open(config['out_file'], 'w', encoding='utf-8') as f:
        f.writelines(data)

def updateFile():
    while True:
        now = datetime.datetime.now().strftime(time)
        text = f'My current MonkeyType PB: {get_pb()}\n'
        timestamp = f'Updated on: {now}\n'
        console_timestamp = '[%H:%M:%S]'
        print(f'{datetime.datetime.now().strftime(console_timestamp)} Updated the file!')
        changeLine(config['out_line'], text)
        if (config['timestamp_line'] >= 0):
            changeLine(config['timestamp_line'], timestamp)
        sleep(config['api_cooldown'])

if __name__ == '__main__':
    print('-'*40 + '\nWelcome to PBFetcher by skill3472!\n' + '-'*40)
    updateFile()