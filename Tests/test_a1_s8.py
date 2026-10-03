def test_amazon (page):
    page.goto("https://www.amazon.in/")
    side_menu=page.locator("//span[@class='hm-icon-label']")
    side_menu.click()
    page.wait_for_timeout(5000)
    sub_categories = page.locator("//div[contains(@class,'hmenu-item hmenu-title')][text()='Digital Content and Devices']/..//ul/li/a").filter(visible=True).all_inner_texts()
    
    print("Sub category: ", sub_categories)

    select_category=page.locator("//div[contains(@class,'hmenu-item hmenu-title')][text()='Digital Content and Devices']/..//li[a][2]").first
    select_category.click()
    page.wait_for_timeout(5000)

    

   