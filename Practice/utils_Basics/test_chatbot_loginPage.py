import json
import time
# pytest C:\Users\puchha.pavan\PycharmProjects\PyTest_Python\PlayWright\utils_Basics\test_chatbot_loginPage.py  --tracing on --html=report.html
import pytest
from playwright.sync_api import Page, sync_playwright, expect, Playwright

# # Read the data from external
# # json file
# with open('../data/test_data.json') as f:
#     test_data = json.load(f)
#     print(test_data)
#     users_cred_list = test_data['users_cred']


#need to config with pytest using paramterize
# @pytest.mark.parametrize('user_cred', users_cred_list)
def test_login_with_valid_credentials(browser_context):

    page = browser_context.new_page()

    # Step 1: Navigate to the URL
    page.goto("https://mqa2.xavlab.xyz/")

    # Step 2: Fill in the Email field
    page.get_by_label("Email").fill("puchha.pavan@telusinternational.com")
    # using external file
    # page.get_by_placeholder("Enter email").fill(user_cred["username"])
    page.get_by_role("button").click()

    # Step 3: Wait and fill in the Domain field
    expect(page.get_by_placeholder("Enter domain")).to_be_visible()  # Ensure the field is visible
    page.get_by_placeholder("Enter domain").fill("xd")
    # page.get_by_placeholder("Enter domain").fill(user_cred["domain"])
    page.get_by_role("button").click()

    # Step 4: Wait and fill in the Password field
    expect(page.get_by_placeholder("Enter password")).to_be_visible()  # Ensure the field is visible
    page.get_by_placeholder("Enter password").fill("*Pavan@4331")
    # page.get_by_placeholder("Enter password").fill(user_cred["password"])
    page.get_by_role("button").click()

    # Step 5: Get the current URL after login
    page.wait_for_url("https://mqa2.xavlab.xyz/analytics")
    assert page.url == "https://mqa2.xavlab.xyz/analytics", "Dashboard page URL is incorrect"
    home_page_header = page.get_by_text("Analytics & Reports")  # Replace with a unique text or element
    print(home_page_header)
    expect(home_page_header).to_be_visible()
    time.sleep(5)
    page.get_by_label("Open Chat").click()
    time.sleep(5)
    page.locator("//span[@title='Transaction Bot MQA']").click()
    time.sleep(5)
    page.get_by_placeholder("Ask me something").fill("Explain all Answer cards in the Chat bot")
    time.sleep(5)
    page.locator("//button[@id='msgSenderButton']").click()
    time.sleep(5)
    page.locator("//span[@class='rcw-options-icons cursor close-header']//img").click()
    time.sleep(5)
    page.locator("//button[normalize-space()='Skip']").click()
    time.sleep(5)
    page.locator("//button[normalize-space()='Close']").click()
    time.sleep(5)
    page.locator("//span[@title='Refresh Dashboard']").click()
    time.sleep(5)
    print("The Total count of conversion is ", page.locator("(//h3[@class='report-result'])[1]").text_content())