
import pytest_asyncio
from playwright.async_api import Page, async_playwright

@pytest_asyncio.fixture
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        yield page
        
        await context.close()
        await browser.close()