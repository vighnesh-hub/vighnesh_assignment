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
    page.locator("//*[@id='customer.username']").fill("marval")
    page.locator("//*[@id='customer.password']").fill("123ert")
    page.locator("//*[@id='repeatedPassword']").fill("123ert")
    page.locator("//input[@value='Register']").click()

    assert page.locator("//h1[contains(@class,'title')]/..//p[text()='Your account was created successfully. You are now logged in.']").is_visible()
    page.wait_for_timeout(5000)

    Accounts_overview= page.locator("//a[text()='Accounts Overview']")
    Accounts_overview.click()

    page.wait_for_timeout(5000)
   

    # # Logout
    logout=page.locator("//a[text()='Log Out']")
    logout.click()
    page.wait_for_timeout(5000)
    

    # # Login with new credentials
    # page.locator("//input[@name='username']").fill("vighneshhdfc")
    # page.locator("//input[@name='password']").fill("vighnesh123")
    # page.locator("//input[@value='Log In']").click()

    # # Verify login success
    # assert page.locator("//h1[normalize-space()='Accounts Overview']").is_visible()

    # # Navigate to Bill Payment
    # page.locator("//a[normalize-space()='Bill Payment']").click()

    # # Fill Bill Payment form
    # page.locator("#payee.name").fill("hdfc")
    # page.locator("#payee.address").fill("123 main st")
    # page.locator("#payee.city").fill("anytown")
    # page.locator("#payee.state").fill("CA")
    # page.locator("#payee.zipCode").fill("90210")
    # page.locator("#payee.phoneNumber").fill("1234567890")
    # page.locator("#accountNumber").fill("123456789")
    # page.locator("#verifyAccount[name='verifyAccount']").fill("123456789")
    # page.locator("#amount").fill("100")
    # page.locator("//input[@value='Send Payment']").click()

    # # Verify success message
    # assert page.locator("//h1[normalize-space()='Bill Payment Complete']").is_visible()

    # # Verify transaction history
    # assert page.locator("//td[normalize-space()='hdfc']").is_visible()

    # # Navigate to Request Loan
    # page.locator("//a[normalize-space()='Request Loan']").click()

    # # Fill Loan Application form
    # page.locator("#loanAmount").fill("50000")
    # page.locator("#downAmount").fill("10000")
    # page.locator("//select[@id='fromAccountId']").select_option("12345")  # Assuming account number 12345 exists
    # page.locator("//input[@value='Apply Now']").click()

    # # Verify loan status (success expected for valid inputs)
    # assert page.locator("//td[normalize-space()='50000.00']").is_visible()
    # assert page.locator("//td[normalize-space()='approved']").is_visible()