import requests
import scraper
import time
import json
from datetime import datetime, timedelta

def chunker(seq, size):
  return (seq[pos:pos + size] for pos in range(0, len(seq), size))

class Channel:
  def __init__(self, channel):
    self.name = channel['name'],
    self.oz_bargain_url = channel['oz-bargain-url']
    self.webhook_url = channel['discord-webhook-url']
    self.scraper = scraper.Scraper(self.oz_bargain_url)

  def scrape(self):
    self.scraper.scrape()

  def update(self):
    self.scrape()
    channel_deals = self.scraper.get_formatted_deals()

    if len(channel_deals) > 0:
      print(str(len(channel_deals)) + ' deals for: ' + str(self.oz_bargain_url) + 'channel. \n')

      for group in chunker(channel_deals, 10):
        self.message({
          "color": "0x0099ff",
          "embeds": group
        })
        time.sleep(2.5)

    else:
      self.message({ "content": "No Deals Found." })

    self.send_next_update_interval_message()

  def send_next_update_interval_message(self):
    time_format = '%d %b %y at %I:%M%p'
    timestamp = datetime.now() + timedelta(hours=1)
    formatted_timestamp = timestamp.strftime(time_format)
    next_update_message = '- Deals will be updated in 1 hour at approximately: ' + formatted_timestamp

    self.message({ "content": next_update_message })

  def message(self, payload = {}):
    try:
      if not payload:
        payload = {
          "content": 'No new deals found for ' + self.oz_bargain_url
        }

      headers = {'Content-Type': 'application/json'}
      content = json.dumps(payload)

      return self.handle_message_request(requests.post(self.webhook_url, data=content, headers=headers))
    except Exception as ex:
      print(ex)

  def handle_message_request(self, request_object):
    if not request_object.ok:
      print('Channel Failed to update.')
      print(request_object.status_code)
      print(request_object.reason)
