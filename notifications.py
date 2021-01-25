import config
import twilio_client

class Notifications:
  def __init__(self):
    if config.twilio_active:
      self.twilio_client = twilio_client.TwilioClient()

  def check(self, payload):
    if payload == 'twilio':
      self.check_twilio()

  def check_twilio(self):
    if config.twilio_active:
      self.twilio_client.notify(config.twilio_notification_message)
