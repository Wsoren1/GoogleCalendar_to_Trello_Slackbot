# GoogleCalendar_to_Trello_Slackbot
This software monitors a class schedule, by reading google calendar events, then, pushes a Slack bot to ask if student was assigned any reading, homework, etc.  Student will respond with a name of the assignment, and the day it is due, and then the Software will push a detailed card to trello.




# Features
WIP


# Setup

For python 3.6.5 or greater

### Required Dependicies
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- SlackClient

## Authentication Setup 

#### Run setup.py
This will create a settings file, templates for the credential files for slack and trello, as well as create

#### Setup Google Calendar
[Guide for running first calendarsync.py](https://developers.google.com/calendar/quickstart/python)

With the credentials file:
copy paste and put in credentials.json file

Unfortunately, Google requires a user to go through a web browser, so if on raspberry pi, go to the GUI and then run CalendarSync.py.  This needs to be tested, but I only believe this needs to be done once.  

#### Setup Slack Channel
WIP

#### Setup Trello Board
WIP

## Identify Tracked Events
(WIP)
Open tracked_events.txt

(Picture of google calendar with events that I want tracked in green, events not tracked in blue)
(tracked_events.txt file that represents google calendar)

## 
