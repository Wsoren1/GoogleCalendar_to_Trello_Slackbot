import datetime as dt
from time import sleep
import Interact
# import CalendarSync
import json


def load_next_event(file):
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
        event_data = data[0].strip('\n')
        event_data = event_data.split('|')
        event_data[0] = dt.datetime.strptime(event_data[0][0:19], '%Y-%m-%dT%H:%M:%S')
    return event_data


def delete_next_event(file):
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)

    with open(file, 'w') as fout:
        fout.writelines(data[1:])

with open('settings.json', 'r') as file:
    settings = json.loads(file.read())
    refresh_time = settings["refresh_time"]


while True:  # loop that bot will run tasks

    sleep(settings["refresh_time"])
