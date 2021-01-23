from .TeaserInstance import TeaserInstance

class TeaserListings:
  def __init__(self, teasers):
    self.teasers = teasers
    self.teaserInstances = []
    self.list = self.list

    self.build_teaser_instances()

  def build_teaser_instances(self):
    for teaser in self.teasers:
      self.teaserInstances.append( TeaserInstance(teaser) )

  def list(self):
    total = len(self.teaserInstances)
    print(str(total) + ' OzBargain deals found.')
    print("\n")

    for teaser in self.teaserInstances:
      if teaser.title and teaser.link:
        print(teaser.title)
        print(teaser.link)
        print('\n')