import config
import twilio.rest

class TwilioClient:
  def __init__(self):
    self.twilio_module = twilio.rest.Client(config.twilio_auth_token, config.twilio_sid)

  def notify(self, payload):
    return self.create_message(payload)

  def create_message(self, payload):
    try:
      self.twilio_module.messages.create(
        to=config.twilio_to,
        from_=config.twilio_from,
        body=payload,
      )

      print('Twilio notification sent.')
    except:
      print('Twilio notification Failed.')
