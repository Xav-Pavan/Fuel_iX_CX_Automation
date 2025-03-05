import logging
import time
import allure  # Import Allure for reporting
from playwright.sync_api import expect
from Practice.Fuel_iX_CX.locators.login_locators import LoginPageLocators
from Practice.Fuel_iX_CX.utils.config import BASE_URL

## this is the login page class
class LoginPage:
    """Handles user login functionality for the application."""

    def __init__(self, page):
        """Constructor to initialize Playwright page instance."""
        self.page = page

    @allure.step("Navigating to the website")
    def navigateToURL(self):
        """Navigates to the application's base URL."""
        logging.info("🌍 Navigating to website...")
        self.page.goto(BASE_URL)

    @allure.step("Logging in with provided credentials")
    def loginDetails(self, userName, domainName, passWord):
        """Performs the login process with provided user credentials."""
        logging.info("🔑 Providing valid credentials and logging in...")
        global locators
        locators = LoginPageLocators(self.page)

        # Step 1: Enter Username
        with allure.step("Entering username"):
            expect(locators.USERNAME_INPUT).to_be_visible()
            locators.USERNAME_INPUT.fill(userName)

        # Step 2: Click Login Button (Proceed to Domain Input)
        with allure.step("Clicking 'Next' after entering username"):
            expect(locators.LOGIN_BUTTON).to_be_enabled()
            locators.LOGIN_BUTTON.click()

        # Step 3: Enter Domain Name
        with allure.step("Entering domain name"):
            expect(locators.DOMAIN_INPUT).to_be_visible()
            locators.DOMAIN_INPUT.fill(domainName)

        # Step 4: Click Login Button (Proceed to Password Input)
        with allure.step("Clicking 'Next' after entering domain"):
            expect(locators.LOGIN_BUTTON).to_be_enabled()
            locators.LOGIN_BUTTON.click()

        # Step 5: Enter Password
        with allure.step("Entering password"):
            expect(locators.PASSWORD_INPUT).to_be_visible() # Ensure the field is visible
            locators.PASSWORD_INPUT.fill(passWord)

        # Step 6: Click Login Button (Final Step)
        with allure.step("Clicking login button to authenticate"):
            logging.info("Clicking login button...")
            expect(locators.LOGIN_BUTTON).to_be_enabled()
            locators.LOGIN_BUTTON.click()

        time.sleep(2)  # Wait for navigation to complete
