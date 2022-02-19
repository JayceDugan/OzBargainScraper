import json
import time
import discord_channel
import boto3
import config

class discordChannels:
  def __init__(self):
    self.channels = []
    self.load()

  def load(self):
    channels_json_data = self.load_data()

    for channel in channels_json_data:
      self.add_channel(channel)

    print('Discord Channels data successfully loaded.')

  def load_data(self):
    session = boto3.Session(
      region_name=config.AWS_REGION,
      aws_access_key_id=config.AWS_ACCESS_KEY_ID,
      aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
      aws_session_token=config.AWS_SESSION_TOKEN
    )

    dynamo = session.resource('dynamodb')
    dynamo_discord_webhooks = dynamo.Table('discord_webhooks')
    scan = dynamo_discord_webhooks.scan()

    return scan['Items']

  def add_channel(self, channel):
    self.channels.append( discord_channel.Channel( channel ) )

  def update(self):
    print('Updating discord channels.')

    for channel in self.channels:
      channel.update()
      time.sleep(5)

