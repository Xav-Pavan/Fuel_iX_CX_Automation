import json
import pytest

from PlayWright.PageObjects.end_to_end import EndToEndUseCase
from PlayWright.PageObjects.login import LoginPage

with open('../data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    users_cred_list = test_data['users_cred']


@pytest.mark.parametrize('user_cred', users_cred_list)
def test_login_with_valid_credentials(browser_context, user_cred):
    userName = user_cred["username"]
    domainName = user_cred["domain"]
    passWord = user_cred["password"]
    page = browser_context

    loginPage = LoginPage(page)  #creating object from page object login page
    use_case = EndToEndUseCase(page)
    loginPage.navigateToURL()
    loginPage.loginDetails(userName, domainName, passWord)
    use_case.end_to_end_use_case()
    