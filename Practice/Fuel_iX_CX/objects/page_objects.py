from Fuel_iX_CX.locators.flowrepository_locator import FlowRepositoryPageLocators
from Fuel_iX_CX.pages.centralrepository_page import CentralRepositoryPage
from Fuel_iX_CX.pages.flowrepository_page import FlowRepositoryPage
from Fuel_iX_CX.pages.intent_page import IntentPage

from Fuel_iX_CX.pages.intenttemplate_page import IntentTemplatePage
from Fuel_iX_CX.utils.imports import *  # Import all necessary modules
from Practice.Fuel_iX_CX.pages.analyticsanddashboard_page import DashBoardPage
from Practice.Fuel_iX_CX.pages.usermanagement_page import UserManagementPage


def initialize_page_objects(page):
    """Function to initialize all page objects and return them as a dictionary."""

    with allure.step("Initializing Page Objects"):
        return {
            "login_page": LoginPage(page),
            "dashboard_page": DashBoardPage(page),
            "centralrepo_page":CentralRepositoryPage(page),
            "flowrepo_page" :FlowRepositoryPage(page),
            "intentTemplate_page":IntentTemplatePage(page),
            "intent_page":IntentPage(page),
            "scb": Schedule_Call_Back_Nodes(page),
            "scb_e": Schedule_Call_Back(page),
            "import_intent": Import_SCB_Intent(page),
            "widget": Schedule_Call_Back_Widget(page),
            "dashboard": Schedule_Call_Back_Dashboard(page),
            "usermanagement": UserManagementPage(page),
        }
