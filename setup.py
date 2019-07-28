if input('Are you sure? If you have data in these files, it will be completely overwritten.').lower() == 'yes':
    with open('local_events', 'w') as file1:
        pass

    with open('missed_events', 'w') as file2:
        pass

    with open('slack_credentials.json', 'w') as scfile:
        sc_template = '{"slack_api_key":"None",\n"active_channel":"None"}'
        scfile.write(sc_template)

    with open('trello_credentials.json', 'w') as trfile:
        tr_template = '{"trello_api_key":"None",\n"trello_token":"None",\n' \
                      '"trello_board_id":"None",\n"trello_list_id":"None",\n' \
                      '"class_label_id":"None"}'
        trfile.write(tr_template)

    with open('settings.json', 'w') as setfile:
        settings_template = '{"timeout":30,\n'\
                            '"bot_user":"jarvis",\n'\
                            '"bot_icon":":satellite:",\n'\
                            '"timedelta_assignment":3,\n'\
                            '"refresh_time":10}'
        setfile.write(settings_template)

