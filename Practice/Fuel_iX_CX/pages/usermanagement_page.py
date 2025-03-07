import logging
import time
import allure  # Import Allure for reporting
from playwright.sync_api import expect

from Practice.Fuel_iX_CX.locators.dashboard_locators import ReportAndAnalyticsDashboardPageLocators
from Practice.Fuel_iX_CX.locators.usermanagement_locator import UserManagementPageLocators


class UserManagementPage:


    def __init__(self, page):
        self.page = page

    @allure.step("Validating Reports and analytics Dashboard page")
    def analytics_Page_Validation(self):
        ## initializing dashboard locator page
        global dashBoardlocators
        dashBoardlocators = ReportAndAnalyticsDashboardPageLocators(self.page)

        ## validating url of dashboard page
        self.page.wait_for_url("https://mqa2.xavlab.xyz/analytics")
        assert self.page.url == "https://mqa2.xavlab.xyz/analytics", "Dashboard page URL is incorrect"

        ## validating Analytics text   present on dashboard page title
        expect(dashBoardlocators.DASHBOARDPAGEVALIDATION_TEXT).to_contain_text("Analytics")

    def user_management_icon(self):
        dashBoardlocators.User_Management_Icon.click()
        print("User management Icon is succesfully clicked")