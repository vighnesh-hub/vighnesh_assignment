
import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import expect

from conftest import BASE_URL, STATE_FILE


# Load .env from the project root
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE)


def test_login_and_save_state(browser):
    email = os.getenv("WEBSHOP_EMAIL")
    password = os.getenv("WEBSHOP_PASSWORD")

    assert email and password, (
        f"Missing WEBSHOP_EMAIL or WEBSHOP_PASSWORD in {ENV_FILE}"
    )

    context = browser.new_context()
    page = context.new_page()

    try:
        page.goto(BASE_URL)

        page.get_by_role("link", name="Log in").click()

        page.locator("#Email").fill(email)
        page.locator("#Password").fill(password)

        page.get_by_role("button", name="Log in").click()

        # Verify successful authentication
        expect(
            page.get_by_role("link", name="Log out")
        ).to_be_visible()

        expect(
            page.get_by_role("link", name="My account")
        ).to_be_visible()

        # Save the authenticated browser state
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        context.storage_state(path=str(STATE_FILE))

        assert STATE_FILE.is_file(), (
            f"State file was not created: {STATE_FILE}"
        )

        print(f"Authenticated state saved to: {STATE_FILE}")

    finally:
        context.close()
