import logging
import time
import allure  # Import Allure for reporting
from playwright.sync_api import expect
from Practice.Fuel_iX_CX.locators.login_locators import LoginPageLocators
from Practice.Fuel_iX_CX.utils.config import BASE_URL

## login page class


class LoginPage:
    """Handles user login functionality for the application."""

    def __init__(self, page):
        """Constructor to initialize Playwright page instance."""
        self.page = page
        self.locators = LoginPageLocators(page)  # ✅ Corrected initialization

    @allure.step("Navigating to the website")
    def navigateToURL(self):
        """Navigates to the application's base URL."""
        logging.info("🌍 Navigating to website...")
        self.page.goto(BASE_URL)

    @allure.step("Logging in with provided credentials")
    def loginDetails(self, userName, domainName, passWord):
        """Performs the login process with provided user credentials."""
        logging.info("🔑 Providing valid credentials and logging in...")

        # Step 1: Enter Username
        with allure.step("Entering username"):
            expect(self.locators.USERNAME_INPUT).to_be_visible()
            self.locators.USERNAME_INPUT.fill(userName)

        # Step 2: Click Login Button (Proceed to Domain Input)
        with allure.step("Clicking 'Next' after entering username"):
            expect(self.locators.LOGIN_BUTTON).to_be_enabled()
            self.locators.LOGIN_BUTTON.click()

        # Step 3: Enter Domain Name
        with allure.step("Entering domain name"):
            expect(self.locators.DOMAIN_INPUT).to_be_visible()  # Ensure the field is visible
            self.locators.DOMAIN_INPUT.fill(domainName)

        # Step 4: Click Login Button (Proceed to Password Input)
        with allure.step("Clicking 'Next' after entering domain"):
            expect(self.locators.LOGIN_BUTTON).to_be_enabled()
            self.locators.LOGIN_BUTTON.click()

        # Step 5: Enter Password
        with allure.step("Entering password"):
            expect(self.locators.PASSWORD_INPUT).to_be_visible()  # Ensure the field is visible
            self.locators.PASSWORD_INPUT.fill(passWord)

        # Step 6: Click Login Button (Final Step)
        with allure.step("Clicking login button to authenticate"):
            logging.info("Clicking login button...")
            expect(self.locators.LOGIN_BUTTON).to_be_enabled()
            self.locators.LOGIN_BUTTON.click()

            time.sleep(2)  # Wait for navigation to complete
            # self.page.goto("https://mqa2.xavlab.xyz/central-repository/1923lzObe40vNPfvY2HPh9bcYnv/2kuhmKLRqKfhHcM7UY53ON5vTwL/flow-template/2tt0lcXjBkMNx0FOTptEJWCtH2J")
            # time.sleep(2)