from slackclient import SlackClient
import random
import time
from AssignmentCard import Card
import datetime as dt
import json


class Error(Exception):
    pass


class UserResponseTimeoutError(Error):
    pass


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


def slack_message(dict_key, extra_text=None):
    sc = SlackClient(slack_api_key)
    sc.api_call('chat.postMessage', channel=settings['slack_channel'],
                text=random.choice(message_dict[dict_key]).format(extra_text),
                username=settings['bot_user'], icon_emoji=settings['bot_icon'])

    # Trellobot Dialogue

    if dict_key == 'ignore_notification':
        time.sleep(5)

        sc.api_call('chat.postMessage', channel=settings['slack_channel'],
                    text=':(',
                    username='TrelloBot', icon_emoji=':computer:')
        time.sleep(5)
        sc.api_call('chat.postMessage', channel=settings['slack_channel'],
                    text=":face_with_rolling_eyes:\nLook, I'll keep a tab open on your missed events, "
                         "I'll ask again later",
                    username=settings['bot_user'], icon_emoji=settings['bot_icon'])


def wait_and_listen():
    if slack_client.rtm_connect():
        start = dt.datetime.now()
        while True:
            # extract user messages
            events = slack_client.rtm_read()
            if dt.datetime.now() - start >= dt.timedelta(minutes=30):
                slack_message('ignore_notification')
                raise UserResponseTimeoutError

            time.sleep(1)
            for event in events:
                if event['type'] == 'message' and event['channel'] == active_channel:
                    try:
                        if event['subtype'] == 'bot_message':
                            pass
                    except KeyError:
                        return event['text']


    with open('missed_events', 'r') as file:
        missed_events_count = 0
        for i in file:
            missed_events_count += 1
        if missed_events_count != 0:
            slack_message('missed_prompt', str(missed_events_count))
            if wait_and_listen().lower() == 'yes':
                for i in range(missed_events_count):
                    calendar_event = load_next_event('missed_events')
                    template_card = Card(calendar_event[1])

                    event_str = "Here's missed class {0}. \n```{1}\n{2}```\n" \
                                "What were you assigned?".format(i + 1,
                                                                 str(calendar_event[1]),
                                                                 str(calendar_event[0]))

                    sc = SlackClient(slack_api_key)
                    sc.api_call('chat.postMessage', channel=settings['slack_channel'],
                                text=event_str,
                                username=settings['bot_user'], icon_emoji=settings['bot_icon'])

                    template_card.title = wait_and_listen()
                    if template_card.title.lower() != 'nothing':
                        slack_message('due_date_prompt')
                        month_date = wait_and_listen()
                        month_date = month_date.split('/')
                        month = int(month_date[0])
                        day = int(month_date[1])
                        year = dt.datetime.now().year

                        due_date = dt.date(year, month, day)

                        due_time = calendar_event[0].time()

                        due_datetime = dt.datetime.combine(due_date, due_time)

                        template_card.due_date = due_datetime

                        template_card.push_to_trello()

                        slack_message('card_pushed')
                        time.sleep(3)

                    if i < missed_events_count:
                        slack_message('more_assignments_prompt')
                        time.sleep(2)
                        missed_events_count -= 1

                    delete_next_event('missed_events')

    slack_message('farewell')


# Move str to config file
with open('slack_credentials.json', 'r') as file:
    credentials = json.loads(file.read())


slack_api_key = credentials["slack_api_key"]
active_channel = credentials["active_channel"]

message_dict = {
    'greeting_prompt': ['Hi! I see you just completed {0}. Did you get any assignments?',
                        'Hey there. Did you get any assignments in {0}?',
                        'Hello, I hope your {0} class went well, is there any homework or reading?',
                        "What's up? I noticed you completed {0}. Any assignments?",
                        'Hey, you just finished your class on {0}, did you get anything I should take note of?'
                        ],

    'user_respond_yes': ['How many assignments did you get?',
                         'What is the damage?',
                         'INSERT INTEGER OF ASSIGNMENT_COUNT.  \nUh... I meant how many did you get?'
                         ],

    'user_respond_no': ['Well, lucky you!',
                        "Well aren't you lucky."
                        ],

    'title_prompt': ['What should I call this assignment?',
                            ],

    'due_date_prompt': ['What day is this assignment due?',
                        ],

    'card_pushed': ['Great, I added that to your Pending Tasks list in your To Do board in Trello.'],

    'more_assignments_prompt': ['Alright, on to the next assignment...'],

    'ignore_notification': ["Don't ignore me you ass. You created me for this. I'm not gonna die like trellobot did."],

    'missed_prompt': ['Hey, I see you have {0} unscheduled events. Would you like to schedule them now?'],

    'farewell': ["Looks like I got down everything I needed to. Good luck on your assignments! "
                 "I'll be watching you :eyes:"]
}
slack_client = SlackClient(slack_api_key)

with open('settings.json', 'r') as file:
    settings = json.loads(file.read())
