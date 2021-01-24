import os
import sys
from twilio.rest import Client

class Twilio:
  def __init__(self):
    self.sid = os.environ['TWILIO_ACCOUNT_SID']
    self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
    self.client = Client(self.sid, self.auth_token)
    self.messages = self.client.messages
    self.send = self.create_message
    self.from_ = "+16786471318"
    self.to = "+61411485436"
    self.characterLimit = 1600

  def create_message(self, payload):
    try:
      print("Attempting to send message: ", payload)
      self.client.messages.create(body=payload, from_=self.from_, to=self.to)
      print('Message sent.')
    except:
      print("Unexpected error during attempt to send text message:", sys.exec_info()[0])


