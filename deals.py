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
    result = ['']

    for teaser in self.teaser_instances:
      teaser_is_valid = teaser.title and teaser.link

      if teaser_is_valid:
        teaser_message = self.build_teaser_message(teaser)
        teaser_message_length = len(teaser_message)
        current_message_length = len(result[-1])
        potential_message_length = teaser_message_length + current_message_length
        character_limit_exceeded = self.check_character_limit(potential_message_length)

        if not character_limit_exceeded:
          result[-1] += teaser_message
        else:
          result.append(teaser_message)

    return result

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