import bs4
import requests
import config
import deals

class Scraper:
  def __init__(self):
    self.domain = config.oz_bargain_domain
    self.request = []
    self.soup = []
    self.deals = []
    self.listings = []
    self.load()

  def load(self):
    self.request = self.make_request()
    self.soup = self.make_soup()
    self.deals = self.get_deals()

    self.build_teaser_listings()
    self.list_deals = self.listings.list


  def make_request(self):
    return requests.get(self.domain)

  def make_soup(self):
    return bs4.BeautifulSoup(self.request.text, 'html.parser')

  def get_deals(self):
    return self.soup.find_all('div', class_="node node-ozbdeal node-teaser")

  def deals_exist(self):
    return len(self.deals) > 0

  def build_teaser_listings(self):
    if self.deals_exist:
      self.listings = deals.Deals(self.deals)