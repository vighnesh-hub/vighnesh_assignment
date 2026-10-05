def test_register(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("//input[@name='username']").fill("marval")
    page.locator("//input[@name='password']").fill("123ert")
    page.locator("//input[@value='Log In']").click()
    page.wait_for_timeout(5000)

    new_account= page.locator("//a[text()='Accounts Overview']")
    new_account.click()

    page.wait_for_timeout(5000)

   