import datetime as dt
from time import sleep
import Interact
import CalendarSync


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


# CalendarSync.main()
schedule_path = 'local_events'
next_event = load_next_event(schedule_path)


while True:
    next_event = load_next_event(schedule_path)
    now = dt.datetime.now()
    today = dt.date.today()
    midnight = dt.datetime.combine(today, dt.datetime.min.time())
    print(next_event)
    print(now)
    if now >= next_event[0]:
        if now - next_event[0] <= dt.timedelta(seconds=15):
            try:
                Interact.calendar_card_creation()
            except Interact.UserResponseTimeoutError:
                with open('missed_events', 'a') as file:
                    file.write(next_event[0].isoformat() + '------|' + next_event[1] + '\n')

            delete_next_event(schedule_path)

    if now >= midnight:
        if now - midnight <= dt.timedelta(seconds=15):
            CalendarSync.main()

    sleep(10)
