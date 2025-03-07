import logging
import allure
import pytest
from Fuel_iX_CX.utils.imports import *  # Import everything from imports.py


@pytest.mark.usefixtures("page_fixture")
def test_verify_invite_user(page_fixture):
    """
    Test to verify the 'Invite user' feature.
    """

    # Fetch test data
    test_data = get_test_data()
    username = test_data["valid_user"]["username"]
    password = test_data["valid_user"]["password"]
    domain = test_data["valid_user"]["domain"]

    # Use the page instance from page_fixture
    page = page_fixture

    # Initialize all page objects using a single function
    pages = initialize_page_objects(page)

    with allure.step("Navigating to Login Page"):
        pages["login_page"].navigateToURL()

    with allure.step(f"Logging in as {username}"):
        pages["login_page"].loginDetails(username, domain, password)

    with allure.step("Dashboard Page"):
        pages["dashboard_page"].analytics_Page_Validation()
        pages["dashboard_page"].click_User_Management_Icon()

    with allure.step("User management Page"):
        pages["usermanagement_page"].click_Invite_User()