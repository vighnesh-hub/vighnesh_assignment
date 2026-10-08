def test_register(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("//a[normalize-space()='Register']").click()
    page.wait_for_timeout(5000)
    page.locator("//*[@id='customer.firstName']").fill("vimal")
    page.locator("//*[@id='customer.lastName']").fill("vighnesh")
    page.locator("//*[@id='customer.address.street']").fill("perambra")
    page.locator("//*[@id='customer.address.city']").fill("Vadakara")
    page.locator("//*[@id='customer.address.state']").fill("Kerala")
    page.locator("//*[@id='customer.address.zipCode']").fill("673524")
    page.locator("//*[@id='customer.phoneNumber']").fill("7034916271")
    page.locator("//*[@id='customer.ssn']").fill("70347483")
    page.locator("//*[@id='customer.username']").fill("vishnu")
    page.locator("//*[@id='customer.password']").fill("m1234")
    page.locator("//*[@id='repeatedPassword']").fill("m1234")
    page.locator("//input[@value='Register']").click()

    assert page.locator("//h1[contains(@class,'title')]/..//p[text()='Your account was created successfully. You are now logged in.']").is_visible()
    page.wait_for_timeout(5000)

    Accounts_overview= page.locator("//a[text()='Accounts Overview']")
    Accounts_overview.click()
     
    Account_number=page.locator("//*[@id='accountTable']/tbody/tr[1]/td[1]/a").inner_text()
    print("Account number: ",Account_number)
    page.wait_for_timeout(5000)
   

    # # Logout
    logout=page.locator("//a[text()='Log Out']")
    logout.click()
    page.wait_for_timeout(5000)
    

    