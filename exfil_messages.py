import os
import requests
import json

token = ""

def get_cursor(chan, cursor):
    messages = requests.post(f"https://slack.com/api/conversations.history?pretty=1&channel={chan}&limit=5000&cursor={cursor}", headers={"Authorization": "Bearer {token}"})
    with open('channel_dump.json', 'a') as json_file:
        json.dump(messages.json(), json_file, indent=4, sort_keys=True)
        json_file.close()
    if "response_metadata" in messages.json():
        get_cursor(chan, messages.json()['response_metadata']['next_cursor'])

def get_message(chan):
    messages = requests.post(f"https://slack.com/api/conversations.history?pretty=1&channel={chan}&limit=5000", headers={"Authorization": "Bearer {token}"})
    with open('channel_dump.json', 'a') as json_file:
        json.dump(messages.json(), json_file, indent=4, sort_keys=True)
        json_file.close()
    if "response_metadata" in messages.json():
        get_cursor(chan, messages.json()['response_metadata']['next_cursor'])


with open("channel_ids", "r") as chan_list:
    for x in chan_list:
        get_message(x.strip())
