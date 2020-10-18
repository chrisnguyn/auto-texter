# Permanent uptime script - i.e. if permanently running on a Raspberry Pi

import os
import random
import schedule
import time
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

twilio_account = os.environ.get('twilio_account')
twilio_token = os.environ.get('twilio_token')
send_to = os.environ.get('send_to')
send_from = os.environ.get('send_from')

client = Client(twilio_account, twilio_token)
TEXTS = ['text_1', 'text_2', 'text_3', 'text_4', 'text_5']


def send_text(message):
    client.messages.create(
        from_=send_from,
        to=send_to,
        body=message
    )
    print('Text sent!')


schedule.every().day.at('01:36').do(send_text, random.choice(TEXTS))  # define a scheduled task - func(), *args, **kwargs
print('Currently running...')

while True:
    schedule.run_pending()  # are there tasks to run at their designated time?
    time.sleep(15)  # don't need to check every second; sleep for 15s
