import pytest
import allure  # Import Allure for reporting

from Fuel_iX_CX.pages.analytics_page import AnalyticsPage
from Fuel_iX_CX.pages.login_page import LoginPage
from Fuel_iX_CX.pages.widget_page import WidgetPage
from Fuel_iX_CX.utils.helpers import get_test_data


@pytest.mark.parametrize("username, password, domain", [
    (get_test_data()["valid_user"]["username"],
     get_test_data()["valid_user"]["password"],
     get_test_data()["valid_user"]["domain"])
])
@allure.feature("Login Functionality")  # Allure Feature Tag
@allure.story("Valid Login Scenario")  # Allure Story Tag
def test_login_with_valid_credentials(page_fixture, username, password, domain):
    """Test case to verify login with valid credentials."""
    page = page_fixture  # Using the corrected fixture

    # Allure: Attach Test Metadata
    allure.attach(f"Username: {username}", name="Test Data", attachment_type=allure.attachment_type.TEXT)

    try:
        # Step 1: Navigate to Login Page
        login_page = LoginPage(page)
        analytics_page = AnalyticsPage(page)
        widget_page = WidgetPage(page)

        with allure.step("Navigate to URL"):
            login_page.navigateToURL()

        with allure.step("Enter Login Credentials"):
            login_page.loginDetails(username, domain, password)

        # Step 2: Validate Analytics Page
        with allure.step("Validate Analytics Page"):
            analytics_page.analyticsPageValidation()

        # Step 3: Validate Widget Page (If needed)
        with allure.step("Validate Widget Page"):
            widget_page.widgetValidation()

        # Allure: Attach Success Message
        allure.attach("Test Passed Successfully", name="Test Status", attachment_type=allure.attachment_type.TEXT)

    except Exception as e:
        # Capture a Screenshot on Failure
        screenshot_path = "reports/screenshots/test_login_failure.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)

        # Log Failure in Allure Report
        allure.attach(str(e), name="Error Message", attachment_type=allure.attachment_type.TEXT)

        # Raise the exception to fail the test
        raise AssertionError("Test Failed: " + str(e))
