# Fire this script as needed - i.e. if being hosted on Heroku and using Heroku Scheduler

import os
import random
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


send_text(random.choice(TEXTS))
