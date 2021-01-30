import json
import time
import discord_channel

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
    with open('lib/discord_channels.json') as discord_channels_json:
      return json.load(discord_channels_json)

  def add_channel(self, channel):
    self.channels.append( discord_channel.Channel( channel ) )

  def update(self):
    print('Updating discord channels.')

    for channel in self.channels:
      channel.update()
      time.sleep(5)

