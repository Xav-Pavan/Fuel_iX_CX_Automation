from Fuel_iX_CX.utils.imports import *
import logging

from playwright.sync_api import expect


class Import_SCB_Intent:
    """Class to handle the importing of Schedule Call Back (SCB) intents in the Playwright UI."""

    def __init__(self, page):
        """Initialize the class with a Playwright page instance."""
        self.page = page

    @allure.step("Importing BA_Schedule_call_back_Scenario Intent")
    def importing_scb_intent(self):
        """Method to navigate and import the SCB intent into the chatbot flow."""

        with allure.step("Navigating to Flow Section"):
            logging.info("🤖 Navigating to the Chatbot section...")
            self.page.locator("//a[@href='/chat-bot']//*[name()='svg']").click()
            self.page.get_by_role("heading", name="Transaction Bot MQA").click()

        with allure.step("Selecting Flow_New_Joinee"):
            self.page.get_by_text("Flow_New_Joinee").click()

        with allure.step("Selecting a node for Import"):
            self.page.locator(
                "div:nth-child(12) > .rst__node > .rst__nodeContent > div > .rst__rowWrapper > .rst__row > "
                ".rst__rowContents > .rst__rowTitleRowToolbar > .rst__rowLabel > .rst__rowTitle > div > "
                ".rst__rowTitle__inner").click()

        with allure.step("Selecting elements for import"):
            self.page.get_by_test_id("virtuoso-item-list").get_by_text("2").click()
            self.page.get_by_test_id("chatbot-icon-btn").locator("img").nth(1).click()
            self.page.get_by_text("Common").click()
            self.page.get_by_text("FLOW", exact=True).click()

        with allure.step("Selecting Flow_New_Joine for import"):
            self.page.get_by_test_id("import-popup-wrapper").get_by_text("Flow_New_Joine").click()
            self.page.get_by_text("one", exact=True).click()
            self.page.get_by_test_id("import-popup-wrapper").get_by_text("2", exact=True).click()

        with allure.step("Selecting first intent from the list"):
            self.page.locator(".intents-list > li").first.click()

        with allure.step("Clicking on Import Button"):
            logging.info("📥 Importing the newly created intent...")
            self.page.get_by_role("button", name="Import").click()
            Import_successfully = self.page.locator("//div[@class='MuiAlert-message css-1xsto0d']").inner_text()
            print(Import_successfully)
            assert Import_successfully == "Templates imported successfully in bot category."
            screenshot_path = r"C:/Users/anshu.sharma/Fuel_iX_CX_Automation/Fuel_iX_CX/BA_UseCases/success_images/test1.png"

            self.page.screenshot(path=screenshot_path)

            print(f"Screenshot saved at: {screenshot_path}")

        with allure.step("Train the Bot"):
            self.page.get_by_test_id("chatbot-icon-btn").locator("img").first.click()
            expect(self.page.locator("//div[normalize-space(text()) ='Train job has been scheduled.']")).to_be_visible(timeout=50000)
            Train_successfully = self.page.locator("//div[@class='MuiAlert-message css-1xsto0d']").inner_text()
            print(Train_successfully)
            assert Train_successfully == "Train job has been scheduled."
            screenshot_path = r"C:/Users/anshu.sharma/Fuel_iX_CX_Automation/Fuel_iX_CX/BA_UseCases/success_images/test2.png"

            self.page.screenshot(path=screenshot_path)

        with allure.step("Verifying success message after bot training"):
            expect(self.page.locator("//div[text()=\"'Transaction Bot MQA' bot trained successfully\"]")) \
                .to_be_visible(timeout=50000)
            Trained_successfully = self.page.locator("//div[@class='MuiAlert-message css-1xsto0d']").inner_text()
            print(Trained_successfully)
            assert Trained_successfully == "'Transaction Bot MQA' bot trained successfully"
            screenshot_path = r"C:/Users/anshu.sharma/Fuel_iX_CX_Automation/Fuel_iX_CX/BA_UseCases/success_images/test3.png"

            self.page.screenshot(path=screenshot_path)

        # Optional validation: Uncomment if required
        # with allure.step("Verifying Open Chat Button is enabled"):
        #    expect(self.page.get_by_label("Open Chat")).to_be_enabled()
