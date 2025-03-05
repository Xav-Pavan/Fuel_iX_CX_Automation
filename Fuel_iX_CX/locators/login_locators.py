# import pytest
#
#
# class LoginPageLocators:
#     USERNAME_INPUT = "Enter email"
#     DOMAIN_INPUT = "Enter domain"
#     PASSWORD_INPUT = "Enter password"
#     LOGIN_BUTTON = "button"
#     DASHBOARDPAGEVALIDATION_TEXT = "//span[@title='Analytics & Reports']"

import pytest


class LoginPageLocators:
    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.USERNAME_INPUT = self.page.get_by_placeholder("Enter email")
        self.DOMAIN_INPUT = self.page.get_by_placeholder("Enter domain")
        self.PASSWORD_INPUT = self.page.get_by_placeholder("Enter password")
        self.LOGIN_BUTTON = self.page.locator("//*[@type='submit']")
