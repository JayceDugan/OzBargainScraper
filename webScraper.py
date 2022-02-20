import asyncio
import aiohttp
import bs4
import json
from deals import Deals
from utils import chunker, load_scraper_config

class WebScraper(object):
    def __init__(self):
        self.config = load_scraper_config()

        asyncio.run(self.main())

    async def extract_deal_teasers(self, text):
        try:
            soup = bs4.BeautifulSoup(text, 'html.parser')
            return soup.find_all('div', class_="node node-ozbdeal node-teaser")
        except Exception as e:
            print(str(e))

    async def message_channel(self, session, config, payload):
        try:
            headers = {'Content-Type': 'application/json'}
            content = json.dumps(payload)

            webhook_url = config['webhook_url']
            webhook_data = content
            response = await session.post(webhook_url, data=webhook_data, headers=headers)

            return response
        except Exception as ex:
            print(ex)

    async def fetch(self, session, config):
        try:
            url = config['oz_bargain_url']

            async with session.get(url) as response:
                text = await response.text()
                teasers = await self.extract_deal_teasers(text)
                teaser_deals = Deals(teasers)
                teaser_embeds = teaser_deals.list()

                message_tasks = []

                if len(teaser_embeds) > 0:
                    for group in chunker(teaser_embeds, 10):
                        message_tasks.append(self.message_channel(session, config, {
                            "color": "0x0099ff",
                            "embeds": group
                        }))
                else:
                    message_tasks.append(
                        self.message_channel(session, config, { "content": "No Deals Found." })
                    )

                await asyncio.gather(*message_tasks)

                return text, url, teasers

        except Exception as e:
            print(str(e))

    async def main(self):
        tasks = []

        async with aiohttp.ClientSession() as session:
            for config in self.config:
                tasks.append(self.fetch(session, config))

            await asyncio.gather(*tasks)