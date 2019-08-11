# GoogleCalendar_to_Trello_Slackbot
This software monitors a class schedule, by reading google calendar events, then, pushes a Slack bot to ask if student was assigned any reading, homework, etc.  Student will respond with a name of the assignment, and the day it is due, and then the Software will push a detailed card to trello.

# Setup

For python 3.6.5 or greater

### Required Dependicies
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- SlackClient v1.2.1

## Authentication Setup 

#### Run setup.py
This will create a settings file, templates for the credential files for slack and trello, as well as create

#### Setup Google Calendar
As oauth 2.0 must be done over a web browser, create a temporary directory with a venv to go through the guide, then extract the token information.

[Guide for running first calendarsync.py](https://developers.google.com/calendar/quickstart/python)


With the credentials file:
copy paste the text and put in google_credentials.json file in the server project directory.

With the token.pickle file:
Transfer the token.pickle file to the server project directory

Open the tracked events file and write your google calendar events (case sensitive) you want to track.

Make sure the user that will be running has write permissions to the files 'local_events' and 'missed_events'

#### Setup Slack Channel
[Get your Slack API Key](https://api.slack.com/custom-integrations/legacy-tokens)

[Find your channel id](https://www.wikihow.com/Find-a-Channel-ID-on-Slack-on-PC-or-Mac)

Then, in the slack_credentials file, input both those keys accordingly.


#### Setup Trello Board
[Get your Trello API Key and Token](https://trello.com/app-key)

Go to your trello board in a web browser, and add `.json` to the end. 

You're looking for three IDs:

Trello Board ID: This id should be the first id in the first line of the file.
Trello List ID: Search the file for the name of the list you want your calendar assignments to appear. Paired with the list name, there should be an ID.
Class Label ID: Search the file for the title of your wanted label. Paired with the title, there should be an ID to copy.
[More info on Custom Labels in trello](https://help.trello.com/article/797-adding-labels-to-cards)

Take all the information recorded, and open trello_credentials.json and input all the IDs and both the Key and Token.

## Run main.py
Configure your server to run main.py on startup, then restart.  Feel free to play around in the settings file, as well as play around with any code.  Hope this helps! 
