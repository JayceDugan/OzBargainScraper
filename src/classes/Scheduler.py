import schedule
import time

from .OzBargain import OzBargain
from .Twilio import Twilio

class Scheduler:
  def __init__(self):
    self.ozBargainInstance = OzBargain()
    self.twilioClient = Twilio()
    print('Scheduler Initialized.')

  def start(self):
    schedule.every().day.at('11:30').do(self.run)
    print('Scheduler Started.')

    while True:
       schedule.run_pending()
       time.sleep(1)

  def run(self):
    print('Scheduler run invoked: ', self.currentTime())
    self.twilioClient.send(self.ozBargainInstance.list_deals())

  def currentTime(self):
    localTime = time.localtime()

    return time.strftime("%H:%M:%S", localTime)