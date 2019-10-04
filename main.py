import os
import sys

from slacker import Slacker

slack_token = os.getenv("SLACK_TOKEN")
slack = Slacker(slack_token)


def channel_list(slack):
    users = slack.users.list().body["members"]
    user_ids = []
    for user in users:
        if not (
            user["is_bot"]
            or user["is_app_user"]
            or user["deleted"]
            or user["is_restricted"]
            or user["name"] == "slackbot"
        ):
            user_ids.append(user['id'])
    return user_ids

channel_id = sys.argv[1]
user_ids = channel_list(slack)
for user_id in user_ids:
    try:
        slack.channels.invite(channel_id, user_id)
    except:
        # already exsit
        print(user_id)
