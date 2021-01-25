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

  def list(self, word_limit = config.oz_teaser_title_word_limit):
    result = ''

    for teaser in self.teaser_instances:
      teaser_is_valid = teaser.title and teaser.link

      if teaser_is_valid:
        result += self.build_teaser_message(teaser, word_limit)

    character_limit_exceeded = self.check_character_limit(result)

    if character_limit_exceeded:
      return self.list(word_limit - 1)
    else:
      return result

  def build_teaser_message(self, teaser, word_limit):
    result = ''
    spacer = '\n'

    result += " ".join(teaser.title.split()[:word_limit])
    result += spacer
    result += pyshorteners.Shortener().tinyurl.short(teaser.link)
    result += spacer
    result += spacer

    return result

  def check_character_limit(self, payload):
    return len(payload) > config.discord_character_limit

  def print(self):
    print(self.list())