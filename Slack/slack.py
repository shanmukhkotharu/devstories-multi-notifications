import os
import logging
import urllib
from botocore.exceptions import ClientError

def slack_basic(channel_id,message):
    # bot token
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    # place url from slack here.
    SLACK_URL = "Replace_this"
    channel_id = slack_event["channel"]
    data = urllib.parse.urlencode(
                (
                    ("token", BOT_TOKEN),
                    ("channel", channel_id),
                    ("text", message)
                )
            )
    data = data.encode("ascii")
    request = urllib.request.Request(
            SLACK_URL,
            data=data,
            method="POST"
        )
    request.add_header(
            "Content-Type",
            "application/x-www-form-urlencoded"
        )
    urllib.request.urlopen(request).read()
