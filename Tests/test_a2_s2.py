def test_register(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("//input[@name='username']").fill("vishnu")
    page.locator("//input[@name='password']").fill("m1234")
    page.locator("//input[@value='Log In']").click()
    page.wait_for_timeout(5000)

    open_account= page.locator("//a[text()='Open New Account']")
    open_account.click()
    
    new_account = page.locator("//input[contains(@class,'button')]")
    new_account.click()

    assert page.locator("//h1[text()='Account Opened!']")
    account_number=page.locator("//*[@id='newAccountId']").text_content()
    print("New account number is:",account_number)
    page.wait_for_timeout(5000)

    #navigate to account overview

    Accounts_overview= page.locator("//a[text()='Accounts Overview']")
    Accounts_overview.click()
    page.wait_for_timeout(5000)

    account_numbers = page.locator("table#accountTable tbody tr td:first-child a").all_text_contents()

#print all account numbers
    print("Account Numbers:")
    for account in account_numbers:
        print(account.strip())

    page.wait_for_timeout(5000)
       
       



   