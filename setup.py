if input('Are you sure? If you have data in these files, it will be completely overwritten.').lower() == 'yes':
    with open('local_events', 'w') as file1:
        pass

    with open('missed_events', 'w') as file2:
        pass

    with open('slack_credentials.json', 'w') as scfile:
        sc_template = '{"slack_api_key":"None", "active_channel":"None"}'
        scfile.write(sc_template)

    with open('trello_credentials.json', 'w') as trfile:
        tr_template = '{"trello_api_key":"None", "trello_token":"None", ' \
                      '"trello_board_id":"None", "trello_list_id":"None", ' \
                      '"class_label_id":"None"}'
        trfile.write(tr_template)

    with open('settings.json', 'w') as setfile:
        pass
