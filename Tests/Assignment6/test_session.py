
from playwright.sync_api import expect

from conftest import BASE_URL


def test_reuse_session_search_book_and_add_to_cart(
    authenticated_context,
):
    page = authenticated_context.new_page()

    # Start a new browser context with the saved session.
    page.goto(BASE_URL)

    # Verify the saved session is authenticated.
    expect(
        page.get_by_role("link", name="Log out")
    ).to_be_visible()

    expect(
        page.get_by_role("link", name="My account")
    ).to_be_visible()

    # Navigate to Books.
    page.goto(f"{BASE_URL}books")

    # Search for a book using the site's search box.
    search_box = page.locator("#small-searchterms")
    search_box.fill("Computing and Internet")
    search_box.press("Enter")

    # Open the matching product from search results.
    product_link = page.get_by_role(
        "link", name="Computing and Internet", exact=True
    ).first

    expect(product_link).to_be_visible()
    product_link.click()

    # Verify that the product page opened.
    expect(
        page.get_by_role(
            "heading", name="Computing and Internet"
        )
    ).to_be_visible()

    # Add the product to the cart.
    add_to_cart = page.get_by_role(
        "button", name="Add to cart"
    )

    if add_to_cart.count() == 0:
        add_to_cart = page.locator(
            "input[value='Add to cart']"
        )

    expect(add_to_cart.first).to_be_visible()
    add_to_cart.first.click()

    # Open the shopping cart.
    page.get_by_role(
        "link", name="Shopping cart"
    ).click()

    # Verify the expected book is in the cart.
    expect(
        page.get_by_text(
            "Computing and Internet", exact=True
        )
    ).to_be_visible()

    print(
        "Session reused successfully. "
        "Book added to the shopping cart."
    )
