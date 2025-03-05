from pytest_playwright.pytest_playwright import page

from PlayWright.Locateors.loginPageLocators import LoginPageLocators
from PlayWright.PageObjects.analytics import AnalyticsPage
from PlayWright.PageObjects.login import LoginPage


class ObjectRepo:
    locators = LoginPageLocators()
    loginPage = LoginPage(page)  # creating object from page object login page
    analyticsPage = AnalyticsPage(page)
