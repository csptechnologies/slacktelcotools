import os
import re
import requests
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()
app = App(
    token=os.environ.get("TOKEN"),
    signing_secret=os.environ.get("SIGNING_SECRET")
)

@app.command("/lookup-cnam")
def lookup(ack, respond, command):
    ack()
    number = command.get("text", "").strip()
    validatenum = bool(re.match(r"^\d{11}$", number))

    if not number or not validatenum:
        respond(
        text = "Please provide a valid 11 digit phone number. Please note this tool only works for Toll Free and United States numbers.", response_type="ephemeral")
        return
    try:
        respond(text=f"Looking up CNAME for {number}...", response_type="ephemeral")
        api = f"https://api.csptech.org/cnam/lookup.php?number={number}"
        response = requests.get(api)
        result = response.text
        respond(text=f"CNAME for {number}: {result}", response_type="in_channel")

    except Exception as e:
        respond(text=f"An error occurred while looking up the CNAME: {str(e)}", response_type="ephemeral")

@app.command("/lookup-lrn")
def lookup(ack, respond, command):
    ack()
    number = command.get("text", "").strip()
    validatenum = bool(re.match(r"^\d{11}$", number))

    if not number or not validatenum:
        respond(
        text = "Please provide a valid 11 digit phone number. Please note this tool only works for Toll Free and United States numbers.", response_type="ephemeral")
        return
    try:
        respond(text=f"Looking up LRN for {number}...", response_type="ephemeral")
        api = f"https://api.csptech.org/cnam/lrn.php?number={number}"
        response = requests.get(api)
        result = response.text
        respond(text=f"LRN for {number}: {result}", response_type="in_channel")

    except Exception as e:
        respond(text=f"An error occurred while looking up the LRN: {str(e)}", response_type="ephemeral")

@app.command("/lookup-cnam-private")
def lookup(ack, respond, command):
    ack()
    number = command.get("text", "").strip()
    validatenum = bool(re.match(r"^\d{11}$", number))

    if not number or not validatenum:
        respond(
        text = "Please provide a valid 11 digit phone number. Please note this tool only works for Toll Free and United States numbers.", response_type="ephemeral")
        return
    try:
        respond(text=f"Looking up CNAME for {number}...", response_type="ephemeral")
        api = f"https://api.csptech.org/cnam/lookup.php?number={number}"
        response = requests.get(api)
        result = response.text
        respond(text=f"CNAME for {number}: {result}", response_type="ephemeral")

    except Exception as e:
        respond(text=f"An error occurred while looking up the CNAME: {str(e)}", response_type="ephemeral")

@app.command("/lookup-lrn-private")
def lookup(ack, respond, command):
    ack()
    number = command.get("text", "").strip()
    validatenum = bool(re.match(r"^\d{11}$", number))

    if not number or not validatenum:
        respond(
        text = "Please provide a valid 11 digit phone number. Please note this tool only works for Toll Free and United States numbers.", response_type="ephemeral")
        return
    try:
        respond(text=f"Looking up LRN for {number}...", response_type="ephemeral")
        api = f"https://api.csptech.org/cnam/lrn.php?number={number}"
        response = requests.get(api)
        result = response.text
        respond(text=f"LRN for {number}: {result}", response_type="ephemeral")

    except Exception as e:
        respond(text=f"An error occurred while looking up the LRN: {str(e)}", response_type="ephemeral")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.start(port=port)