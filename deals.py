import pyshorteners
import oz_teaser
import config

class Deals:
  def __init__(self, deals):
    self.deals = deals
    self.teaser_instances = []
    self.build_teaser_instances()

  def build_teaser_instances(self):
    for deal in self.deals:
      self.teaser_instances.append( oz_teaser.OzTeaser(deal) )

  def list(self):
    result = []

    for teaser in self.teaser_instances:
      teaser_is_valid = teaser.title and teaser.link

      if teaser_is_valid:
        result.append(self.build_teaser_embed(teaser))

    return result

  def build_teaser_embed(self, teaser):
    return {
      "title": teaser.title,
      # "url": pyshorteners.Shortener().tinyurl.short(teaser.link),
      "url": teaser.link,
      "thumbnail": {
        "url": teaser.thumbnail_src,
      }
    }

  def build_teaser_message(self, teaser):
    result = '\n'
    spacer = '\n'

    result += teaser.title + ' - <' + pyshorteners.Shortener().tinyurl.short(teaser.link) + '>'
    result += spacer

    return result

  def check_character_limit(self, payload):
    return payload > config.discord_character_limit

  def print(self):
    print(self.list())