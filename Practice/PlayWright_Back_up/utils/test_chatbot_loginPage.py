import json

import pytest
from playwright.sync_api import Page, sync_playwright, expect, Playwright

from PlayWright.PageObjects.analytics import AnalyticsPage
from PlayWright.PageObjects.login import LoginPage
from PlayWright.PageObjects.widget import WidgetPage

# Read the data from external
# json file
with open('../data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    users_cred_list = test_data['users_cred']


#need to config with pytest using paramterize
@pytest.mark.parametrize('user_cred', users_cred_list)
def test_login_with_valid_credentials(browser_context, user_cred):
    userName = user_cred["username"]
    domainName = user_cred["domain"]
    passWord = user_cred["password"]
    page = browser_context


    #Login Page
    loginPage = LoginPage(page)  #creating object from page object login page
    analyticsPage = AnalyticsPage(page)
    widgetPage = WidgetPage(page)
    loginPage.navigateToURL()
    loginPage.loginDetails(userName, domainName, passWord)

    #Analytics Page
    analyticsPage.analyticsPageValidation()
