
import logging
import time
import allure  # Import Allure for reporting
from playwright.sync_api import expect
from Fuel_iX_CX.locators.dashboard_locators import ReportAndAnalyticsDashboardPageLocators


class DashBoardPage:


    def __init__(self, page):
        self.page = page

    @allure.step("Validating Reposrts and analytics Dashboard page")
    def analytics_Page_Validation(self):
        ## initializing dahboard locator page
        global dashBoardlocators
        dashBoardlocators = ReportAndAnalyticsDashboardPageLocators(self.page)

        ## validating url of dashboard page
        self.page.wait_for_url("https://mqa2.xavlab.xyz/analytics")
        assert self.page.url == "https://mqa2.xavlab.xyz/analytics", "Dashboard page URL is incorrect"

        ## validating Analytics text   present on dashboard page title
        expect(dashBoardlocators.DASHBOARDPAGEVALIDATION_TEXT).to_contain_text("Analytics")

    def click_central_repository_icon(self):
        dashBoardlocators.CENTRAL_REPOSITORY_ICON.click()
        print("Cenrtal Repository Icon is succesfully clicked")