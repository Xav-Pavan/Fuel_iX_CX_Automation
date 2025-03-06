import logging
import time
import allure
from playwright.sync_api import expect

from Fuel_iX_CX.locators.centralrepository_locator import CentralRepositoryPageLocators


class CentralRepositoryPage:


    def __init__(self, page):
        self.page = page



    def click_flowtype_central_repository_icon(self):
        ## initializing instance of centralrepository_locator class
        global centralrepolocators
        centralrepolocators=CentralRepositoryPageLocators(self.page)

        centralrepolocators.FLOW_REPOSITORY_BUTTON.click()
        print(" Flow type Central Repository Icon is successfully clicked")