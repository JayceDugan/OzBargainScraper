import schedule
import time
import discord_client
import scraper

class Scheduler:
  def __init__(self):
    self.discordClient = discord_client.DiscordClient()
    print('Scheduler Initialized.')

  def start(self):
    self.run()
    schedule.every().hour.do(self.run)
    print('Scheduler Started.')

    while True:
       schedule.run_pending()
       time.sleep(1)

  def run(self):
    self.discordClient.update()