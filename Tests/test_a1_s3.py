
def test_cart(page):
    page.goto("https://demowebshop.tricentis.com/")
    product=page.locator("xpath=//ul[@class='top-menu']//a[contains ( text(), 'Jewelry')]")
    product.click()
    #print("product name: ",product.inner_text())
    price="130.00"
    #price_locator=(f"xpath=//span[@class='price actual-price' and text()='{price}']")
    add_to_cart=page.locator(f"xpath=//span[@class='price actual-price' and text()='{price}']/ancestor::div[contains(@class, 'product-item')]//input[@value='Add to cart']")
    add_to_cart.click()
    page.wait_for_timeout(5000)


    # Navigate to the cart 
    page.locator("xpath=//*[@id='topcartlink']/a/span[1]").click()
    page.wait_for_timeout(5000)
   
   
    
