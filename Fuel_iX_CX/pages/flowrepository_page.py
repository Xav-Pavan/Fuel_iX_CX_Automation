import logging
import time
import allure
from playwright.sync_api import expect

from Fuel_iX_CX.locators.flowrepository_locator import FlowRepositoryPageLocators


class FlowRepositoryPage:


    def __init__(self, page):
        self.page = page



    def navigate_to_new_folder_to_add_new_intent(self):
        ## initializing instance of centralrepository_locator class
        global flowrepolocators
        flowrepolocators=FlowRepositoryPageLocators(self.page)

        logging.info("📂 Navigating to Central Repository...")
        flowrepolocators.FLOW_NEW_JOINEE_FOLDER.click()
        flowrepolocators.ONE_SUB_FOLDER.click()
        flowrepolocators.SECOND_SUB_FOLDER.click()
        flowrepolocators.BTN_CLICK.click()
        flowrepolocators.STYL_BTN_NEW_INTENT.click()

