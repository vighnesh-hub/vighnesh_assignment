
import logging

from playwright.sync_api import expect

from conftest import BASE_URL

logger = logging.getLogger("webshop")


def test_task3_logging_screenshot_and_trace(page):
    logger.info("Opening Demo Web Shop")
    page.goto(BASE_URL)

    logger.info("Verifying home page loaded")
    expect(page).to_have_title("Demo Web Shop")

    logger.info("Checking the Log in link")
    expect(
        page.get_by_role("link", name="Log in")
    ).to_be_visible()

    logger.info("Task 3 test steps completed successfully")
