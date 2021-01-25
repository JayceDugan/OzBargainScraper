import config
import requests
import notifications
import json

class DiscordClient:
  def __init__(self):
    self.notification_services = notifications.Notifications()

  def send_message(self, payload):
    request = self.send_message_request(payload)
    self.handle_message_request(request)

  def send_message_request(self, payload):
    try:
      headers = { 'Content-Type': 'application/json' }
      content = json.dumps({ "content": payload })

      return requests.post( config.discord_webhook_url, data=content, headers=headers )
    except:
      print('Unexpected error occurred attempting to send discord message.')

  def handle_message_request(self, request_object):
    if request_object.ok:
      print('Discord message successfully sent.')
      self.notification_services.check('twilio')

    else:
      print('Discord message failed with status code: ', request_object.status_code, " because of: ", request_object.reason)
