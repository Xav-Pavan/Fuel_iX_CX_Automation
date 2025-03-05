import logging
import allure
import pytest
from Fuel_iX_CX.utils.imports import *  # Import everything from imports.py


@pytest.mark.usefixtures("page_fixture")
def test_verify_the_schedule_call_back(page_fixture):
    """
    Test to verify the 'Schedule Call Back' feature.
    """

    # Fetch test data
    test_data = get_test_data()
    username = test_data["valid_user"]["username"]
    password = test_data["valid_user"]["password"]
    domain = test_data["valid_user"]["domain"]

    # Use the page instance from page_fixture
    page = page_fixture

    # Initialize all page objects using a single function
    pages = initialize_page_objects(page)

    with allure.step("Navigating to Login Page"):
        pages["login_page"].navigateToURL()

    with allure.step(f"Logging in as {username}"):
        pages["login_page"].loginDetails(username, domain, password)

    with allure.step("Dashboard Page"):
        pages["dashboard_page"].analytics_Page_Validation()
        pages["dashboard_page"].click_central_repository_icon()

    with allure.step("Central Repository Page"):
        pages["centralrepo_page"].click_flowtype_central_repository_icon()

    with allure.step("New Intent Template Inside Flow Repo"):
        pages["flowrepo_page"].navigate_to_new_folder_to_add_new_intent()
        pages["intentTemplate_page"].add_template_name_to_new_intent()
        pages["intent_page"].creating_schedule_callback_scenerio_get_available_slots_node(
            "Schedule_Callback_Get_Available_Slots",
            "Please allocate the earliest possible time slot for a scheduled call", "this is test scb"
        )
        pages["intent_page"].creating_schedule_new_callBack_request_node(
            "Schedule_New_CallBack_Request",
            "Run Schedule_New_CallBack_Request node",
            "Submit call back"
        )
        pages["intent_page"].creating_booking_success_node(
            "Booking_Success",
            "Run booking success node",
            "This is booking success"
        )
        pages["intent_page"].creating_reschedule_callBack_request_node(
            "Reschedule_CallBack_Request",
            "Run Reschedule_CallBack_Request node",
            "This is reschedule"
        )
        pages["intent_page"].creating_issue_occured_node(
            "Issue_Occured",
            "Run Issue_Occured node",
            "Issue occurred"
        )
        pages["intent_page"].creating_callBack_booking_failed_node(
            "CallBack_Booking_Failed",
            "CallBack_Booking_Failed node",
            "Booking failed"
        )
        pages["intent_page"].creating_canceling_callBack_request_node(
            "Canceling_CallBack_Request",
            "Run Canceling_CallBack_Request node",
            "This is cancel"
        )

