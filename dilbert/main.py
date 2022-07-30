import logging
import os
import re

import validators
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="Dilbert")
logger = logging.getLogger(__name__)


@app.message(re.compile("doi"))  # type: ignore
def show_random_joke(message, say):
    # channel_type = message["channel_type"]
    # channel = message["channel"]
    blocks = message["blocks"]
    for block in blocks:
        for block_elements in block["elements"]:
            for element in block_elements["elements"]:
                if element["type"] == "link":
                    print(element["url"])


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
