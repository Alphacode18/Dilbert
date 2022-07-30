import os
import re
import logging
import requests
import shortuuid

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="Dilbert")
logger = logging.getLogger(__name__)


@app.message(re.compile("doi"))  # type: ignore
def doi_listener(message, say):
    # channel_type = message["channel_type"]
    channel = message["channel"]
    blocks = message["blocks"]
    for block in blocks:
        for block_elements in block["elements"]:
            for element in block_elements["elements"]:
                if element["type"] == "link":
                    url = element["url"]
                    data = requests.get(url)
                    name = shortuuid.uuid(name=url) + ".pdf"
                    with open(name, "wb") as output:
                        output.write(data.content)
    say(text=f"Processed as {name}", channel=channel)


@app.message(re.compile(".*"))
def catch_all(message, say):
    # channel_type = message["channel_type"]
    channel = message["channel"]
    say(text="Hi, I don't know what to do with this", channel=channel)


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
