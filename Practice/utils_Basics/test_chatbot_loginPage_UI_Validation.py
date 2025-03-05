import time

from playwright.sync_api import Page, sync_playwright, expect

def test_login_with_valid_credentials(page: Page):
    # Step 1: Navigate to the URL
    page.goto("https://mqa2.xavlab.xyz/")

    # Step 2: Fill in the no Email field
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    expect(page.get_by_text('Please enter Email.')).to_be_visible()
    error_message_1 = page.get_by_text('Please enter Email.')
    print(error_message_1)
    if error_message_1.__eq__('Please enter Email.'):
        print("No Email Error message is validate successfully")
    else:
        print("No Email Error message is not valid")
    time.sleep(5)

    # Step 3: Fill in the Invalid Domain Email field
    page.get_by_label("Email").fill("123.com")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    error_message = page.get_by_text("Email is not valid.")
    expect(error_message).to_be_visible()
    time.sleep(5)

    # Step 4: Fill in the Invalid Email field
    page.get_by_label("Email").fill("puchha.pavan@gmail.com")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    error_message = page.get_by_text("Something Went Wrong")
    expect(error_message).to_be_visible()
    print(error_message)
    if error_message.__eq__("Something Went Wrong"):
        print("Invalid Email Error message is validate successfully")
    else:
        print("Invalid Email Error message is not valid")
    time.sleep(5)


    # Step 5: Wait and fill in No Domain field
    page.get_by_label("Email").fill("puchha.pavan@telusinternational.com")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    expect(page.get_by_placeholder("Enter domain")).to_be_visible()
    expect(page.get_by_role("button")).to_be_enabled()# Ensure the field is visible
    page.get_by_role("button").click()
    error_message2 = page.get_by_text("Please enter domain")
    expect(error_message2).to_be_visible()
    print(error_message2)
    time.sleep(5)

    # Step 6: Wait and fill in InValid Domain field
    page.get_by_placeholder("Enter domain").fill("1xd")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    error_message3 = page.get_by_text("Invalid Domain")
    expect(error_message3).to_be_visible()
    print(error_message3)
    time.sleep(5)

    # Step 7: Wait and Click on Forgot Domain Link
    expect(page.get_by_title("Forgot Domain"))
    page.get_by_title("Forgot Domain").click()
    expect(page.get_by_placeholder("Enter email"))
    page.get_by_placeholder("Enter email").fill("puchha.pavan@telusinternational.com")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    success_message1 = page.get_by_text("an email with list of user domains has been sent to the registered email address")
    expect(success_message1).to_be_visible()
    print(success_message1)
    time.sleep(5)



    # Step 8: Wait and fill in the No Password field
    expect(page.get_by_text('Please enter Email.'))
    page.get_by_label("Email").fill("puchha.pavan@telusinternational.com")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    expect(page.get_by_placeholder("Enter domain"))
    page.get_by_placeholder("Enter domain").fill("xd")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    expect(page.get_by_placeholder("Enter password")).to_be_visible()
    expect(page.get_by_role("button")).to_be_enabled()# Ensure the field is visible
    page.get_by_role("button").click()
    error_message4 = page.get_by_text("Please enter password")
    expect(error_message4).to_be_visible()
    print(error_message4)
    time.sleep(5)

    # Step 9: Wait and fill in the InValid Password field
    page.get_by_placeholder("Enter password").fill("*Pavan@123")
    expect(page.get_by_role("button")).to_be_enabled()
    page.get_by_role("button").click()
    error_message5 = page.get_by_text("Authentication Failed")
    expect(error_message5).to_be_visible()
    print(error_message5)
    time.sleep(5)

    # Step 10: Wait and click on Forgot Password link
    expect(page.get_by_title("Forgot Password"))
    page.get_by_title("Forgot Password").click()
    expect(page.get_by_placeholder("Enter email"))
    page.get_by_placeholder("Enter email").fill("puchha.pavan@telusinternational.com")
    page.get_by_role("button").click()
    expect(page.get_by_placeholder("Domain"))
    page.get_by_placeholder("Domain").fill("xd")
    page.get_by_role("button").click()
    success_message2 = page.get_by_text("A verification email has been sent to your email")
    expect(success_message2).to_be_visible()
    print(success_message2)
    time.sleep(5)
