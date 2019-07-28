import datetime as dt
import requests
import json


class Card:
    def __init__(self, desc, title=None, due_datetime=None):
        self.desc = desc
        self.title = title
        self.due_date = due_datetime
        self.default_due_time = dt.timedelta(hours=3)
        self.due_datetime = None

    def push_to_trello(self):
        self.due_datetime = self.due_date - self.default_due_time

        # Move to config file
        with open('trello_credentials.json', 'r') as file:
            credentials = json.loads(file.read())

        api_key = credentials["trello_api_key"]
        token = credentials["trello_token"]

        to_do_id = credentials["trello_board_id"]
        pending_tasks = credentials["trello_list_id"]
        class_label_id = credentials["class_label_id"]
        authentication = '?key={0}&token={1}'.format(api_key, token, to_do_id)

        url = "https://api.trello.com/1/cards" + authentication

        querystring = {"name": self.title, "desc": self.desc, "due": self.due_datetime, "idList": pending_tasks,
                       "keepFromSource": "all", "idLabels": class_label_id}

        requests.request("POST", url, params=querystring)
