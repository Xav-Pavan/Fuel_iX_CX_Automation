import logging
import time
import allure
from playwright.sync_api import expect

# from Fuel_iX_CX.locators.intent_locators import IntentPageLocators
from Practice.Fuel_iX_CX.locators.intent_locators import IntentPageLocators


class IntentPage:

    def __init__(self, page):

        self.page = page

    def add_text_card(self, text_msg):
        intentlocators.ADD_CARDS_LINK.click()
        intentlocators.TEXT_CARD_BUTTON_ICON.click()
        intentlocators.INPUT_TEXT_TEXT_CARD.fill(text_msg)
        intentlocators.ADD_CARDS_LINK.click()


    def node_creation(self,NodetemplateTitle,nodequestion,textcardmsg):
        ## initializing instance of centralrepository_locator class
        global intentlocators
        intentlocators = IntentPageLocators(self.page)
        # self.page.pause()
        intentlocators.NODE_TEMPLATE_TITLE.fill(NodetemplateTitle)
        intentlocators.NODE_QUESTION.fill(nodequestion)
        self.add_text_card(textcardmsg)

        # Wait for up to 2 sec
        self.page.wait_for_timeout(500)
        # intentlocators.SAVE_BUTTON.wait_for(state="visible", timeout=2000)  # Wait for up to 2 sec
        intentlocators.SAVE_BUTTON.click()


        actual_newnode_sucessmsg = intentlocators.NODE_TEMPLATE_CREATION_SUCCESS_MSG.inner_text()
        Expected__newnode_sucessmsg = "Template Created Successfully."
        assert actual_newnode_sucessmsg == Expected__newnode_sucessmsg, "Assertionfailed"
        print(f"{NodetemplateTitle} is successfully created and validated")



    def creating_schedule_callback_scenerio_get_available_slots_node(self, NodetemplateTitle, nodequestion, textcardmsg):

        self.node_creation(NodetemplateTitle,nodequestion, textcardmsg)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_schedule_new_callBack_request_node(self, NodetemplateTitle, nodequestion,textcardmsg):
        self.page.locator("//div[@class='rst__rowNodeAdd add-node-uid'][1]").click()
        self.page.get_by_text("New Node").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_booking_success_node(self, NodetemplateTitle, nodequestion,textcardmsg):
        self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[2]").click()
        self.page.get_by_text("New Node").nth(1).click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_reschedule_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[3]").click()
        self.page.locator("(//div[@class='flowMenuItem'][normalize-space()='New Node'])[3]").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_issue_occured_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.get_by_test_id("add-btn-flow").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_callBack_booking_failed_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.get_by_test_id("add-btn-flow").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_canceling_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.get_by_test_id("add-btn-flow").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()









