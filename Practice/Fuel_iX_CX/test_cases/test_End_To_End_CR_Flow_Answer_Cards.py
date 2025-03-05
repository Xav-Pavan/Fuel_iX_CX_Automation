import pytest

from Fuel_iX_CX.pages.sample_test import EndToEndUseCase
from Fuel_iX_CX.pages.login_page import LoginPage
from Fuel_iX_CX.utils.helpers import get_test_data


@pytest.mark.parametrize("username, password, domain",
                         [(get_test_data()["valid_user"]["username"],
                           get_test_data()["valid_user"]["password"],
                           get_test_data()["valid_user"]["domain"])])
def test_login_with_valid_credentials(page_fixture, username, password, domain):
    page = page_fixture

    loginPage = LoginPage(page)  #creating object from page object login page
    use_case = EndToEndUseCase(page)
    loginPage.navigateToURL()
    loginPage.loginDetails(username, domain, password)
    use_case.end_to_end_use_case()
    