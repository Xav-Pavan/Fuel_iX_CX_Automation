from playwright.sync_api import expect

from Fuel_iX_CX.utils.imports import *
from Fuel_iX_CX.data.test_SCB_data import SCB_TestData
import os

class Schedule_Call_Back_Dashboard:
    """Class to handle the Schedule Call Back Dashboard interactions in the Playwright UI."""

    def __init__(self, page):
        """Initialize the class with a Playwright page instance."""
        self.page = page

    @allure.step("Navigating through the Schedule Call Back Dashboard")
    def dashboard(self):
        """Automates the navigation and interaction with the dashboard."""

        # Step 1: Click on 'Analytics and Reports' section
        self.page.locator("//li[@data-tip='Analytics and Reports']").click()

        # Step 2: Click on the 'Refresh Dashboard' button
        expect(
            self.page.locator("//span[@title='Refresh Dashboard']//img[@class='chatbot-header-icon']")).to_be_visible(
            timeout=60000)
        self.page.locator("//span[@title='Refresh Dashboard']//img[@class='chatbot-header-icon']").click()

        # Step 3: Click on the first interactive element in the dashboard
        expect(self.page.locator("(//span[@class='hand'])[1]")).to_be_visible(timeout=50000)
        self.page.locator("(//span[@class='hand'])[1]").click()

        # Step 4: Click to expand and view all transactional details
        expect(self.page.locator("(//span[@title='Click to see all transactional details'])[1]")).to_be_visible(
            timeout=50000)
        self.page.locator("(//span[@title='Click to see all transactional details'])[1]").click()

        # Step 5: Capture a full-page screenshot for verification
        # screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH)
        # self.page.screenshot(path=screenshot_path, full_page=True)
        # allure.attach.file(screenshot_path, name="Dashboard Screenshot", attachment_type=allure.attachment_type.PNG)
        # Ensure the directory exists
        os.makedirs(SCB_TestData.SCREENSHOT_PATH, exist_ok=True)

        # Define the full screenshot path
        screenshot_filename = "dashboard_screenshot"
        screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, f"{screenshot_filename}{SCB_TestData.FILE_TYPE}")

        # Capture screenshot
        self.page.screenshot(path=screenshot_path, full_page=True)

        # Attach screenshot to Allure report
        allure.attach.file(screenshot_path, name="Dashboard Screenshot", attachment_type=allure.attachment_type.PNG)
