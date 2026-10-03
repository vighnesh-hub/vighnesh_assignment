from playwright.sync_api import Page, expect

def test_assignment1_scenario1(page):

    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Books").first.click()
    product_name = "Fiction"

    add_to_cart=page.locator(f"xpath=//div[contains(@class, 'product-item')][.//h2/a[normalize-space()='{product_name}']]//input[@value='Add to cart']")
    
    add_to_cart.click()
 
    # Navigate to the cart 
    page.locator("xpath=//*[@id='topcartlink']/a/span[1]").click()
   
    # Verify the product is listed in the cart
    cart_product = page.locator(f"xpath=//tr[contains(@class, 'cart-item-row')]//a[@class='product-name' and normalize-space()='{product_name}']")
    expect(cart_product).to_be_visible()
  
    
       