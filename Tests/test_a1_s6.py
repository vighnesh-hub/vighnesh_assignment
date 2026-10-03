def test_amazon (page):
    page.goto("https://www.amazon.in/")
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("books")
    page.get_by_role("searchbox", name="Search Amazon.in").press("Enter")
    page.wait_for_timeout(5000)

    product_name=page.locator("//div[contains(@class,'a-section a-spacing-small a-spacing-top-small')]/..//span[text()='The Psychology of Money']")
    product_name.click()
    page.wait_for_timeout(5000)
    cart=page.locator("//span[contains(@class,'a-button-inner')]/..//input[@name='submit.add-to-cart']")
    cart.click()
    page.wait_for_timeout(5000)