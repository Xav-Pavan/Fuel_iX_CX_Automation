from Fuel_iX_CX.utils.imports import *
from Fuel_iX_CX.data.test_SCB_data import SCB_TestData
from Fuel_iX_CX.locators.scb_usecase_locators import ScheduleCallBackLocators
import logging
import os


class Schedule_Call_Back_Nodes:
    """Class to handle the creation and management of Schedule Call Back nodes in the Playwright UI."""

    def __init__(self, page):
        """Initialize the class with a Playwright page instance and locators."""
        self.page = page
        self.locators = ScheduleCallBackLocators(page)

    @allure.step("Navigating to CR New Intent")
    def navigateCR_New_Intent(self):
        """Navigate to the 'New Intent' section within the flow."""
        logging.info("📂 Navigating to Central Repository...")
        self.locators.NAVIGATE_CR_NEW_INTENT.click()
        self.locators.FLOW_LINK.click()
        self.locators.FLOW_NEW_JOINE.click()
        self.locators.FLOW_ONE.click()
        self.locators.FLOW_TWO.click()
        logging.info("📁 Navigating to the specific folder...")
        self.locators.BTN_CLICK.click()
        logging.info("📝 Creating a new intent...")
        self.locators.NEW_INTENT_BUTTON.click()
        self.locators.INTENT_INPUT_BOX.fill(SCB_TestData.INTENT_NAME)
        self.locators.INTENT_OK_BUTTON.click()
        self.locators.ADD_BTN_FLOW.click()

    def create_node(self, template_title, message_text, text_fill, success_message, screenshot_filename):
        """
        Generic function to create a node with custom inputs.

        :param template_title: Title of the node template
        :param message_text: Message to be filled in the node
        :param text_fill: Response text for the node
        :param success_message: Expected success message
        :param screenshot_filename: Name of the screenshot file
        """

        self.locators.TEMPLATE_TITLE_INPUT.fill(template_title)
        self.locators.RICH_TEXT_AREA.click()
        self.locators.RICH_TEXT_AREA.fill(message_text)
        self.locators.ADD_CARDS_BUTTON.click()
        self.locators.TEXT_OPTION.click()
        self.locators.PRE_DIV_FIRST.click()
        self.locators.PRE_DIV_FIRST.fill(text_fill)
        self.page.wait_for_timeout(500)
        self.locators.SAVE_BUTTON.click()

        # Validate success message
        actual_message = self.locators.NODE_CREATION_SUCCESS_MESSAGE.inner_text()
        print(actual_message)
        assert actual_message == success_message, f"Expected: {success_message}, but got: {actual_message}"

        # Save screenshot

        #  screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH,
        screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, f"{screenshot_filename}{SCB_TestData.FILE_TYPE}")
        self.page.screenshot(path=screenshot_path)

        # print(f"Screenshot saved at: {screenshot_path}")

        self.page.wait_for_timeout(500)
        self.locators.BACK_BUTTON.click()

    @allure.step("Creating 'Schedule Callback Get Available Slots' Node")
    def creating_Schedule_Callback_Get_Available_Slots_Node(self):
        """Create a node to get available slots for scheduling a callback."""
        self.create_node(
            template_title=SCB_TestData.FIRST_NODE_NAME,
            message_text=SCB_TestData.FIRST_NODE_QUESTION,
            text_fill=SCB_TestData.FIRST_NODE_ANSWER,
            success_message=SCB_TestData.EXPECTED_NODE_CREATE_SUCCESS,
            screenshot_filename="creating_Schedule_Callback_Get_Available_Slots_Node_successfully"

        )
        self.locators.NEW_NODE_CLICK.click()
        self.locators.NEW_NODE_TEXT.click()

    @allure.step("Creating 'Schedule New Callback Request' Node")
    def creating_Schedule_New_CallBack_Request_Node(self):
        """Create a node for scheduling a new callback request."""
        self.create_node(
            template_title=SCB_TestData.SECOND_NODE_NAME,
            message_text="Please select a slot for scheduling a new callback request",
            text_fill=SCB_TestData.SECOND_NODE_ANSWER,
            success_message=SCB_TestData.EXPECTED_NODE_CREATE_SUCCESS,
            screenshot_filename="creating_Schedule_New_CallBack_Request_Node_successfully"
        )
        self.locators.NEW_NODE_CLICK_2.click()
        self.locators.BOOKING_SUCCESS_NEW_NODE.click()

    @allure.step("Creating 'Booking Success' Node")
    def creating_Booking_Success_Node(self):
        """Create a node to handle booking success confirmation."""
        self.create_node(
            template_title=SCB_TestData.THIRD_NODE_NAME,
            message_text="Your booking is confirmed",
            text_fill=SCB_TestData.THIRD_NODE_ANSWER,
            success_message=SCB_TestData.EXPECTED_NODE_CREATE_SUCCESS,
            screenshot_filename="creating_Booking_Success_Node_successfully"
        )
        self.locators.RESCHEDULE_CALLBACK_NODE.click()
        self.locators.RESCHEDULE_FLOW_MENU_ITEM.click()

    @allure.step("Creating 'Reschedule Callback Request' Node")
    def creating_Reschedule_CallBack_Request_Node(self):
        """Create a node for rescheduling an existing callback request."""
        self.create_node(
            template_title=SCB_TestData.FOURTH_NODE_NAME,
            message_text="Please reschedule the callback",
            text_fill=SCB_TestData.FOURTH_NODE_ANSWER,
            success_message=SCB_TestData.EXPECTED_NODE_CREATE_SUCCESS,
            screenshot_filename="creating_Reschedule_CallBack_Request_Node_successfully"
        )
        self.locators.ISSUE_OCCURRED_ADD_BTN_FLOW.click()

    @allure.step("Creating 'Issue Occurred' Node")
    def creating_Issue_Occurred_Node(self):
        """Create a node to handle issues occurring during callback booking."""
        self.create_node(
            template_title=SCB_TestData.FIFTH_NODE_NAME,
            message_text="An issue occurred while processing your request",
            text_fill=SCB_TestData.FIFTH_NODE_ANSWER,
            success_message=SCB_TestData.EXPECTED_NODE_CREATE_SUCCESS,
            screenshot_filename="creating_Issue_Occurred_Node_successfully"
        )
        self.locators.CALLBACK_BOOKING_FAILED_ADD_BTN_FLOW.click()

    @allure.step("Creating 'Callback Booking Failed' Node")
    def creating_CallBack_Booking_Failed_Node(self):
        """Create a node to handle failed callback booking scenarios."""
        self.create_node(
            template_title=SCB_TestData.SIXTH_NODE_NAME,
            message_text="Callback booking failed. Please try again",
            text_fill=SCB_TestData.SIXTH_NODE_ANSWER,
            success_message=SCB_TestData.EXPECTED_NODE_CREATE_SUCCESS,
            screenshot_filename="creating_CallBack_Booking_Failed_Node_successfully"
        )
        self.locators.CANCELING_CALLBACK_ADD_BTN_FLOW.click()

    @allure.step("Creating 'Canceling Callback Request' Node")
    def creating_Canceling_CallBack_Request_Node(self):
        """Create a node to handle cancellation of scheduled callback requests."""
        self.create_node(
            template_title=SCB_TestData.SEVENTH_NODE_NAME,
            message_text="The callback request has been canceled",
            text_fill=SCB_TestData.SEVENTH_NODE_ANSWER,
            success_message=SCB_TestData.EXPECTED_NODE_CREATE_SUCCESS,
            screenshot_filename="creating_Canceling_CallBack_Request_Node_successfully",

        )
