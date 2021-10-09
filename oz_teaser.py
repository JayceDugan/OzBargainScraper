import config

class OzTeaser:
    def __init__(self, teaser):
        self.title = teaser.find('h2', class_="title")['data-title']
        self.link = config.oz_bargain_domain.rstrip("/") + teaser.find('h2', class_="title").find('a')['href']
        self.thumbnail_src = teaser.find('div', class_="foxshot-container").find('img')['src']
        self.thumbnail_alt = teaser.find('div', class_="foxshot-container").find('img')['alt']
