from Fuel_iX_CX.utils.imports import *  # Import everything from imports.py
import logging


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

    with allure.step("Creating Schedule Callback Nodes"):
        pages["scb"].navigateCR_New_Intent()
        pages["scb"].creating_Schedule_Callback_Get_Available_Slots_Node()
        pages["scb"].creating_Schedule_New_CallBack_Request_Node()
        pages["scb"].creating_Booking_Success_Node()
        pages["scb"].creating_Reschedule_CallBack_Request_Node()
        pages["scb"].creating_Issue_Occurred_Node()
        pages["scb"].creating_CallBack_Booking_Failed_Node()
        pages["scb"].creating_Canceling_CallBack_Request_Node()

    with allure.step("Editing Schedule Callback Nodes"):
        pages["scb_e"].editing_Schedule_Callback_Get_Available_Slots_Node()
        pages["scb_e"].editing_Schedule_New_CallBack_Request_Node()
        pages["scb_e"].editing_Booking_Success_Node()
        pages["scb_e"].editing_Reschedule_CallBack_Request_Node()
        pages["scb_e"].editing_Issue_Occurred_Node()
        pages["scb_e"].editing_Canceling_CallBack_Request_Node()
        pages["scb_e"].editing_CallBack_Booking_Failed_Node()

    with allure.step("Importing the Intent"):
        pages["import_intent"].importing_scb_intent()

    with allure.step("Schedule CallBack Widget"):
        pages["widget"].connecting_with_widget()

    with allure.step("Dashboard"):
        pages["dashboard"].dashboard()
