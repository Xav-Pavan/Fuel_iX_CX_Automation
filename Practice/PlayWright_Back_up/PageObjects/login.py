import logging

from playwright.sync_api import expect

from PlayWright.Locateors.loginPageLocators import LoginPageLocators


class LoginPage:
    # constractor
    def __init__(self, page):
        self.page = page

    def navigateToURL(self):
        logging.info("Navigating to website...")
        self.page.goto("https://mqa2.xavlab.xyz/")

    def loginDetails(self, userName, domainName, passWord):
        locators = LoginPageLocators()
        expect(self.page.get_by_placeholder(locators.USERNAME_INPUT)).to_be_visible()
        self.page.get_by_placeholder(locators.USERNAME_INPUT).fill(userName)

        expect(self.page.get_by_role(locators.LOGIN_BUTTON)).to_be_enabled()
        self.page.get_by_role(locators.LOGIN_BUTTON).click()

        expect(self.page.get_by_placeholder(locators.DOMAIN_INPUT)).to_be_visible()  # Ensure the field is visible
        self.page.get_by_placeholder(locators.DOMAIN_INPUT).fill(domainName)

        expect(self.page.get_by_role(locators.LOGIN_BUTTON)).to_be_enabled()
        self.page.get_by_role(locators.LOGIN_BUTTON).click()

        expect(self.page.get_by_placeholder(locators.PASSWORD_INPUT)).to_be_visible()  # Ensure the field is visible
        self.page.get_by_placeholder(locators.PASSWORD_INPUT).fill(passWord)

        logging.info("Clicking login button...")
        expect(self.page.get_by_role(locators.LOGIN_BUTTON)).to_be_enabled()
        self.page.get_by_role(locators.LOGIN_BUTTON).click()
