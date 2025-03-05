
from Fuel_iX_CX.utils.imports import *  # Import all necessary modules


def initialize_page_objects(page):
    """Function to initialize all page objects and return them as a dictionary."""

    with allure.step("Initializing Page Objects"):
        return {
            "login_page": LoginPage(page),
            "scb": Schedule_Call_Back_Nodes(page),
            "scb_e": Schedule_Call_Back(page),
            "import_intent": Import_SCB_Intent(page),
            "widget": Schedule_Call_Back_Widget(page),
            "dashboard": Schedule_Call_Back_Dashboard(page),
        }
