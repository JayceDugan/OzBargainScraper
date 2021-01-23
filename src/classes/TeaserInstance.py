from ..lib.config import ozBargainDomain

class TeaserInstance:
  def __init__(self, teaser):
    self.instance = teaser
    self.title = self.instance.find('h2', class_="title")['data-title']
    self.link = ozBargainDomain + self.instance.find('a')['href']
