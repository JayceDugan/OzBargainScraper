import config
from twilio.rest import Client

class TwilioClient:
  def notify(self, payload):
    return self.create_message(payload)

  def create_message(self, payload):
    try:
      client = Client(config.twilio_auth_token, config.twilio_sid)

      client.messages.create(
        body=payload,
        from_=config.twilio_from,
        to=config.twilio_to
      )

      print('Twilio notification sent.')
    except:
      print('Twilio notification Failed.')
