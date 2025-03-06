from Fuel_iX_CX.utils.imports import *
import logging

from playwright.sync_api import expect


class Schedule_Call_Back_Widget:
    """Class to handle the editing of Schedule Call Back nodes in the Playwright UI."""

    def __init__(self, page):
        """Initialize the class with a Playwright page instance."""
        self.page = page

    @allure.step("Connecting with the widget and scheduling a call back")
    def connecting_with_widget(self):
        """Automates the chat interaction for scheduling a call back using the widget."""

        # Step 1: Open Chat Widget
        logging.info("💬 Launching the widget...")
        expect(self.page.get_by_label("Open Chat")).to_be_enabled()
        self.page.get_by_label("Open Chat").click()

        # Step 2: Select the 'Transaction Bot MQA'
        expect(self.page.locator("//span[@title='Transaction Bot MQA']")).to_be_visible()
        self.page.locator("//span[@title='Transaction Bot MQA']").click()
        # Waiting for the bot to load

        # Step 3: Request for the earliest possible time slot
        expect(self.page.locator("(//input[@id='user-input-message'])[1]")).to_be_visible(timeout=50000)
        self.page.locator("(//input[@id='user-input-message'])[1]").fill("Please allocate the earliest possible time slot for a scheduled call")
        self.page.locator("(//button[@id='msgSenderButton'])[1]").click()

        # Step 4: Provide user name (e.g., Hulk)

        expect(self.page.locator("//span[@class='displayed-text']//b[contains(text(),'So we know who to ask for, what is your name?')]")).to_be_visible(timeout=60000)
        self.page.locator("(//input[@id='user-input-message'])[1]").fill("Hulk")
        expect(self.page.locator("(//button[@id='msgSenderButton'])[1]")).to_be_enabled(timeout=50000)
        self.page.locator("(//button[@id='msgSenderButton'])[1]").click()


        # Step 5: Provide phone number

        expect(self.page.locator("//span[@class='displayed-text']//b[contains(text(),'Next, please enter the phone number you want us to')]")).to_be_visible(timeout=60000)
        self.page.locator("(//input[@id='user-input-message'])[1]").fill("9988778655")
        expect(self.page.locator("(//button[@id='msgSenderButton'])[1]")).to_be_enabled(timeout=50000)
        self.page.locator("(//button[@id='msgSenderButton'])[1]").click()

        # Step 6: Select the first available callback slot
        expect(self.page.locator("//ul[@class='list-group']/li[1]")).to_be_visible(timeout=60000)
        self.page.locator("//ul[@class='list-group']/li[1]").click()

        # Step 7: Extract and print the callback confirmation message
        expect(self.page.locator("(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[4]")).to_be_visible(
            timeout=50000)
        callback_value = self.page.locator("(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[4]").inner_text()
        print(f"Initial Callback Confirmation: {callback_value}")

        # Step 8: Click 'Reschedule' button
        expect(self.page.locator("(//button[normalize-space()='Reschedule'])[1]")).to_be_visible(timeout=60000)
        self.page.locator("(//button[normalize-space()='Reschedule'])[1]").click()

        # Step 9: Select the second available callback slot
        expect(self.page.locator("//ul[@class='list-group']/li[2]")).to_be_visible(timeout=60000)
        self.page.locator("//ul[@class='list-group']/li[2]").click()

        # Step 10: Extract and print the rescheduled callback confirmation message
        expect(self.page.locator("(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[6]")).to_be_visible(
            timeout=50000)
        next_callback_value = self.page.locator(
            "(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[6]").inner_text()
        print(f"Rescheduled Callback Confirmation: {next_callback_value}")

        # Step 11: Cancel the scheduled callback
        expect(self.page.locator("(//button[contains(@title,'Cancel')][normalize-space()='Cancel'])[2]")).to_be_visible(timeout=60000)
        self.page.locator("(//button[contains(@title,'Cancel')][normalize-space()='Cancel'])[2]").click()

        # Step 12: Click on the tooltip options
        expect(self.page.locator("div[class='tooltip1'] div[class='rcw-options-icons cursor'] svg")).to_be_visible(
            timeout=50000)
        self.page.locator("div[class='tooltip1'] div[class='rcw-options-icons cursor'] svg").click()


        # Step 13: Skip feedback and close the widget
        expect(self.page.locator("(//button[normalize-space()='Skip'])[1]")).to_be_visible(timeout=60000)
        self.page.locator("(//button[normalize-space()='Skip'])[1]").click()
        expect(self.page.locator("(//button[normalize-space()='Close'])[1]")).to_be_enabled(timeout=60000)
        self.page.locator("(//button[normalize-space()='Close'])[1]").click()

