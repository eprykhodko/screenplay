import asyncio

from aiohttp import ClientSession
from lxml import html

from .constants import BASE_PATH, INDEX_PAGE, SEASON_EPISODES_XPATH


async def fetch_page(url, session):
    async with session.get(url) as response:
        return await response.text(errors='ignore')


async def crawl(show):
    async with ClientSession() as session:
        page_text = await fetch_page(INDEX_PAGE + show, session)
        tasks = [
            asyncio.create_task(fetch_page(BASE_PATH + item.get('href'), session))
            for item
            in html.fromstring(page_text).xpath(SEASON_EPISODES_XPATH)
        ]
        return await asyncio.gather(*tasks)


def gather_pages(show):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(crawl(show))
