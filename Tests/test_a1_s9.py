def test_webshop(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").click()
    page.locator("#small-searchterms").fill("Health Book")
    page.locator("#small-searchterms").press("ArrowDown")
    page.locator("#small-searchterms").press("Enter")
    page.wait_for_timeout(5000)

    product_link = page.locator("//h2[@class='product-title']/a[normalize-space()='Health Book']")
    product_link.click()
    
    # Wait for the specific <h1> to appear on the details page
    page.wait_for_selector("//div[@class='product-name']/h1")

    # NOW your original locator will work perfectly
    product_name = page.locator("//div[contains(@class,'product-name')]//h1[1]")
    print("Product Name:", product_name.inner_text().strip())

    

    product_price=page.locator("//div[contains(@class,'product-price')][2]")
    print("Product Price:", product_price.inner_text().strip())
    page.locator("//input[@class='button-1 add-to-cart-button']").click()
    page.wait_for_timeout(5000)
    page.locator("//div[@class='header-links']/.//li['cart-label'][3]").click()
    page.wait_for_timeout(5000)
