def test_rating(page):
 page.goto("https://demowebshop.tricentis.com/")

 category=page.locator("//div[contains(@class,'block-category-navigation')]//li/a[normalize-space()='Electronics']")
 category.click()

 product=page.locator("//div[contains(@class,'sub-category-grid')]//h2/a[normalize-space()='Camera, photo']")
 product.click()

 choose_product=page.locator("//div[contains(@class,'product-grid')]//h2/a[text()='High Definition 3D Camcorder']")
 choose_product.click()

 product_name=page.locator("xpath=//div[contains(@class,'product-name')]//h1[1]")
 print("Product Name:", product_name.inner_text().strip())
 
 rating_locator=page.locator("xpath=//div[@class='product-review-links'] //a[1]")

 print("Rating:", rating_locator.inner_text().strip())

 page.wait_for_timeout(5000)
