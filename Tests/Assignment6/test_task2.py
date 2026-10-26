#scenario 1
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
    page.locator("//*[@id='customer.username']").fill("amal")
    page.locator("//*[@id='customer.password']").fill("m1234")
    page.locator("//*[@id='repeatedPassword']").fill("m1234")
    page.locator("//input[@value='Register']").click()

    assert page.locator("//h1[contains(@class,'title')]/..//p[text()='Your account was created successfully. You are now logged in.']").is_visible()
    page.wait_for_timeout(5000)

    # Logout
    logout=page.locator("//a[text()='Log Out']")
    logout.click()
    page.wait_for_timeout(5000)
    
    #scenario 2

    #login
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("//input[@name='username']").fill("amal")
    page.locator("//input[@name='password']").fill("m1234")
    page.locator("//input[@value='Log In']").click()
    page.wait_for_timeout(5000)

     # all available account numbers
    all_accounts = page.locator("#accountTable tbody tr td:first-child a").all_text_contents()

    #Account overview
    Accounts_overview= page.locator("//a[text()='Accounts Overview']")
    Accounts_overview.click()
     
    Account_number=page.locator("//*[@id='accountTable']/tbody/tr[1]/td[1]/a").inner_text()
    print("Account number: ",Account_number)
    page.wait_for_timeout(5000)
   
    # print only two account numbers
    account1 = all_accounts[0].strip()
    account2 = all_accounts[1].strip()

    print("Account number 1:", account1)
    print("Account number 2:", account2)
    page.wait_for_timeout(2000)

    #Transfer fund
    transfer_fund = page.locator("//a[text()='Transfer Funds']")
    transfer_fund.click()
    page.wait_for_timeout(2000)
    
    #Enter amount
    amount = page.locator("//*[@id='amount']")
    amount.fill("50")
    page.wait_for_timeout(2000)

    # Select accounts
    page.locator("//*[@id='fromAccountId']").select_option("14121")
    page.locator("//*[@id='toAccountId']").select_option("16008")
    
    transfer= page.locator("//input[@value='Transfer']")
    transfer.click()
    page.wait_for_timeout(5000)

    #verify the amount trasferd

    page.locator("//*[@id='showResult']").wait_for(state="visible")
    
    title_text = page.locator("//*[@id='showResult']/h1").inner_text()
    amount = page.locator("//*[@id='amountResult']  ").inner_text()
    from_acc = page.locator("//*[@id='fromAccountIdResult']").inner_text()
    to_acc = page.locator("//*[@id='toAccountIdResult']").inner_text()
    
    print(f"Status: {title_text}")
    print(f"Amount Transferred: {amount}")
    print(f"From Account: #{from_acc}")
    print(f"To Account: #{to_acc}")

    #navigate to toaccount

    page.locator("//a[text()='Accounts Overview']").click()
    page.wait_for_timeout(2000)
    page.locator("//a[text()='41538']").click()
    page.wait_for_timeout(2000)

   
    

    