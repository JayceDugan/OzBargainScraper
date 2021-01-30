import config

class OzTeaser:
  def __init__(self, teaser):
    self.title = teaser.find('h2', class_="title")['data-title']
    self.link = config.oz_bargain_domain + teaser.find('a')['href']