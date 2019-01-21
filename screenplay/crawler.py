import asyncio

from aiohttp import ClientSession
from lxml import html

from .constants import BASE_PATH, INDEX_PAGE, SEASON_EPISODES_XPATH


async def fetch_page(url, session):
    async with session.get(url) as response:
        return await response.text(errors="ignore")


async def crawl(show):
    async with ClientSession() as session:
        page_text = await fetch_page(INDEX_PAGE + show, session)
        tasks = [
            fetch_page(BASE_PATH + item.get("href"), session)
            for item in html.fromstring(page_text).xpath(SEASON_EPISODES_XPATH)
        ]
        return await asyncio.gather(*tasks)


def gather_pages(show):
    return asyncio.run(crawl(show))
