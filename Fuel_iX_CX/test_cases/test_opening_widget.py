import pytest

from Fuel_iX_CX.pages.analytics_page import AnalyticsPage
from Fuel_iX_CX.pages.login_page import LoginPage
from Fuel_iX_CX.pages.widget_page import WidgetPage
from Fuel_iX_CX.utils.helpers import get_test_data


@pytest.mark.parametrize("username, password, domain",
                         [(get_test_data()["valid_user"]["username"],
                           get_test_data()["valid_user"]["password"],
                           get_test_data()["valid_user"]["domain"])])
def test_login_with_valid_credentials(page_fixture, username, password, domain):
    page = page_fixture

    #Login Page
    loginPage = LoginPage(page)  #creating object from page object login page
    analyticsPage = AnalyticsPage(page)
    widgetPage = WidgetPage(page)
    loginPage.navigateToURL()
    loginPage.loginDetails(username, domain, password)

    #Analytics Page
    analyticsPage.analyticsPageValidation()

    #widget chat
    widgetPage.openTheWidget()
