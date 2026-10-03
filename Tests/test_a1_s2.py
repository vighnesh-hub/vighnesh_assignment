# from playwright.sync_api import sync_playwright


# with sync_playwright() as p:

#     browser = p.chromium.launch(headless=False)

#     page = browser.new_page()

#     page.goto("https://www.amazon.in/")
#     page.wait_for_timeout(5000)
#     side_menu=page.locator("xpath=//*[@id='nav-hamburger-menu']/span")
   
#     side_menu.click()
#     page.wait_for_timeout(2000)

#     headings = page.locator("xpath=//*[@id='hmenu-content']/div[1]/section")

#     count = headings.count()

#     print("Count:",count)
#     print("Main Headings:")

#     for i in range(count):
#         heading = headings.nth(i).inner_text().strip()
#         print(heading)

#     browser.close()

from playwright.sync_api import sync_playwright

def test_amazon_menu_headings():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.amazon.in/")
        page.wait_for_timeout(5000)
        
        # Click the side menu
        menu = page.locator("xpath=//*[@id='nav-hamburger-menu']/span")
        menu.click()
        page.wait_for_timeout(2000)

        # located visible menu
        headings = page.locator("xpath=//*[@id='hmenu-content']//div[contains(@class, 'hmenu-visible')]//section[contains(@class, 'category-section')]")

        print("\n--- Main Headings ---")
        
        for i in range(headings.count()):
            heading_text = headings.nth(i).get_attribute("aria-labelledby")
            print(heading_text)

        browser.close()