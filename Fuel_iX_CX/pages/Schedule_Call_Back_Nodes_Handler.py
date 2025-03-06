from Fuel_iX_CX.utils.imports import *
import logging


class Schedule_Call_Back_Nodes:
    """Class to handle the creation and management of Schedule Call Back nodes in the Playwright UI."""

    def __init__(self, page):
        """Initialize the class with a Playwright page instance."""
        self.page = page

    # @allure.step("Navigating to CR New Intent")
    # def navigateCR_New_Intent(self):
    #     """Navigate to the 'New Intent' section within the flow."""
    #     logging.info("📂 Navigating to Central Repository...")
    #     self.page.get_by_text("Flow_New_Joine").click()
    #     self.page.get_by_text("one", exact=True).click()
    #     self.page.get_by_text("2", exact=True).click()
    #     logging.info("📁 Navigating to the specific folder...")
    #     self.page.get_by_test_id("btn-click").click()
    #     logging.info("📝 Creating a new intent...")
    #     self.page.get_by_test_id("styl-btn").get_by_text("New Intent").click()
    #     self.page.get_by_test_id("promptinputbox").fill("BA_Schedule_call_back_Scenario")
    #     self.page.get_by_test_id("promptokbutton").click()
    #     self.page.get_by_test_id("add-btn-flow").click()

    @allure.step("Creating 'Schedule Callback Get Available Slots' Node")
    def creating_Schedule_Callback_Get_Available_Slots_Node(self):
        """Create a node to get available slots for scheduling a callback."""
        self.page.get_by_placeholder("Enter template title here").fill("Schedule_Callback_Get_Available_Slots")
        self.page.locator(".questions-rich-text-area").click()
        self.page.locator(".questions-rich-text-area").fill(
            "Please allocate the earliest possible time slot for a scheduled call")
        self.page.get_by_role("button", name="Add   Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        self.page.locator("pre div").first.click()
        self.page.locator("pre div").first.fill("this is test scb")
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_test_id("backbutton-btn").click()

    @allure.step("Creating 'Schedule New Callback Request' Node")
    def creating_Schedule_New_CallBack_Request_Node(self):
        """Create a node for scheduling a new callback request."""
        self.page.locator("//div[@class='rst__rowNodeAdd add-node-uid'][1]").click()
        self.page.get_by_text("New Node").click()
        self.page.get_by_placeholder("Enter template title here").fill("Schedule_New_CallBack_Request")
        self.page.get_by_role("button", name="Add   Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        self.page.get_by_role("paragraph").click()
        self.page.locator("pre div").first.fill("submit call back")
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_test_id("backbutton-btn").click()

    @allure.step("Creating 'Booking Success' Node")
    def creating_Booking_Success_Node(self):
        """Create a node to handle booking success confirmation."""
        self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[2]").click()
        self.page.get_by_text("New Node").nth(1).click()
        self.page.get_by_placeholder("Enter template title here").fill("Booking_Success")
        self.page.get_by_role("button", name="Add   Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        self.page.get_by_role("paragraph").click()
        self.page.locator("pre div").first.fill("this is booking success")
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_test_id("backbutton-btn").click()

    @allure.step("Creating 'Reschedule Callback Request' Node")
    def creating_Reschedule_CallBack_Request_Node(self):
        """Create a node for rescheduling an existing callback request."""
        self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[3]").click()
        self.page.locator("(//div[@class='flowMenuItem'][normalize-space()='New Node'])[3]").click()
        self.page.get_by_placeholder("Enter template title here").fill("Reschedule_CallBack_Request")
        self.page.get_by_role("button", name="Add   Cards").click()
        self.page.locator("#react-tabs-13").get_by_test_id("text").locator("i").click()
        self.page.get_by_role("paragraph").click()
        self.page.locator("pre div").first.fill("this is reschedule")
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_test_id("backbutton-btn").click()

    @allure.step("Creating 'Issue Occurred' Node")
    def creating_Issue_Occured_Node(self):
        """Create a node to handle issues occurring during callback booking."""
        self.page.get_by_test_id("add-btn-flow").click()

        self.page.get_by_placeholder("Enter template title here").fill("Issue_Occured")

        self.page.get_by_role("button", name="Add   Cards").click()

        self.page.get_by_text("Text", exact=True).click()

        self.page.get_by_role("paragraph").click()

        self.page.locator("pre div").first.fill("issue occurred")
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_test_id("backbutton-btn").click()

    @allure.step("Creating 'Callback Booking Failed' Node")
    def creating_CallBack_Booking_Failed_Node(self):
        """Create a node to handle failed callback booking scenarios."""
        self.page.get_by_test_id("add-btn-flow").click()

        self.page.get_by_placeholder("Enter template title here").fill("CallBack_Booking_Failed")

        self.page.get_by_role("button", name="Add   Cards").click()

        self.page.get_by_text("Text", exact=True).click()

        self.page.get_by_role("paragraph").click()

        self.page.locator("pre div").first.fill("booking failed")
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_test_id("backbutton-btn").click()

    @allure.step("Creating 'Canceling Callback Request' Node")
    def creating_Canceling_CallBack_Request_Node(self):
        """Create a node to handle cancellation of scheduled callback requests."""
        self.page.get_by_test_id("add-btn-flow").click()
        self.page.get_by_placeholder("Enter template title here").fill("Canceling_CallBack_Request")
        self.page.get_by_text("AUTO REPLYTAGSSelect...").click()
        self.page.get_by_role("button", name="Add   Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        self.page.get_by_role("paragraph").click()

        self.page.locator("pre div").first.fill("this is cancel")
        self.page.wait_for_timeout(500)
        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_timeout(500)
        self.page.get_by_test_id("backbutton-btn").click()
