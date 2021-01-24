import os
import sys
from twilio.rest import Client

class Twilio:
  def __init__(self):
    self.sid = os.environ['TWILIO_ACCOUNT_SID']
    self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
    self.from_ = os.environ['TWILIO_FROM']
    self.to = os.environ['TWILIO_TO']
    self.client = Client(self.sid, self.auth_token)
    self.messages = self.client.messages
    self.send = self.create_message
    self.characterLimit = 1600

  def create_message(self, payload):
    try:
      self.client.messages.create(body=payload, from_=self.from_, to=self.to)
      print('Twilio Message successfully sent.')
    except:
      print("Unexpected error occurred.")


