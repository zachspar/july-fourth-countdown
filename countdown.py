#!/usr/bin/env python3
"""
Fourth of July Countdown - SMS

Requirements: A Fourth of July countdown text message sent to an outgoing list.
Author: Zachary Spar <zachspar@gmail.com>
Date: April 30, 2021
"""
from config import (TWILIO_AUTH_TOKEN, TWILIO_ACCT_SID, OUTGOING_LIST,
                    SENDING_NUMBER)
from datetime import datetime
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def main():
    """Orchestrate calculating countdown, and sending to outgoing list."""
    now = datetime.now()
    if now <= datetime(month=7, day=4, year=now.year):
        year = now.year
    else:
        year = now.year + 1
    then = datetime(month=7, day=4, year=year)
    diff = then - now
    num_days = diff.days
    print(f"There are {num_days} days until July 4th")
    client = Client(TWILIO_ACCT_SID, TWILIO_AUTH_TOKEN)
    for number in OUTGOING_LIST:
        print(f"Sending countdown message to {number}")
        try:
            message = client.messages.create(body=num_days,
                                             from_=SENDING_NUMBER,
                                             to=str(number))
            print(f"Message has been sent :: {message.sid}")
        except TwilioRestException as e:
            print(e)
            print(f"ERROR: Could not send quote to phone number {number}")


if __name__ == '__main__':
    main()

