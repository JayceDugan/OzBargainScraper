import schedule
import time
import discord
import scraper

class Scheduler:
  def __init__(self):
    self.scraper = scraper.Scraper()
    self.discordClient = discord.DiscordClient()
    print('Scheduler Initialized.')

  def start(self):
    schedule.every().day.at('8:30').do(self.run)

    print('Scheduler Started.')

    while True:
       schedule.run_pending()
       time.sleep(1)

  def run(self):
    print('Scheduler run fired: ', self.currentTime())
    self.discordClient.send_message(self.scraper.list_deals())

  def currentTime(self):
    return time.strftime("%H:%M:%S", time.localtime())