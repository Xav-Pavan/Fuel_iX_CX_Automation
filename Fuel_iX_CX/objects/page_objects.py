import allure

from Fuel_iX_CX.utils.import_settings import *


def initialize_page_objects(page):
    """Initialize all page objects and return them as a dictionary."""

    with allure.step("Initializing Page Objects"):
        return {
            "login_page": LoginPage(page),
            "scb_page": SCBPage(page),
            "dashboard_page": DashBoardPage(page),
            "centralrepo_page": CentralRepositoryPage(page),
            "flowrepo_page": FlowRepositoryPage(page),
            "intentTemplate_page": IntentTemplatePage(page),

        }
