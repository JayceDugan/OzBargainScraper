import requests
import scraper
import json
from datetime import datetime, timedelta

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
      print(str(len(channel_deals)) + ' messages for: ' + str(self.oz_bargain_url) + 'channel. \n')

      for deal_message in channel_deals:
        self.message(" - Current deals listed at: " + str(self.oz_bargain_url) + "\n" + deal_message)
    else:
      self.message('OzCrawler found no new details at this time.')

    self.send_next_update_interval_message()

  def send_next_update_interval_message(self):
    time_format = '%d-%m-%Y %I:%M %p'
    timestamp = datetime.utcnow() + timedelta(hours=1)
    formatted_timestamp = timestamp.strftime(time_format)
    next_update_message = '- Channel Update Successful. \n \n New deals will be posted in an hour at approximately: ' + formatted_timestamp

    self.message(next_update_message)

  def message(self, payload = ''):
    try:
      if not payload:
        payload = 'No new deals found for ' + self.oz_bargain_url

      payload += '\n\n'

      headers = {'Content-Type': 'application/json'}
      content = json.dumps({"content": payload})

      return self.handle_message_request(requests.post(self.webhook_url, data=content, headers=headers))
    except Exception as ex:
      print(ex)

  def handle_message_request(self, request_object):
    if not request_object.ok:
      print('Channel Failed to update.')
      print(request_object.status_code)
      print(request_object.reason)

