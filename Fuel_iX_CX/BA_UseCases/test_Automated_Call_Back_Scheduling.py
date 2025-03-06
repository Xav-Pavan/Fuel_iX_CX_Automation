from Fuel_iX_CX.utils.helpers import get_scb_test_data
from Fuel_iX_CX.utils.imports import *  # Import everything from imports.py
import logging


# @pytest.mark.parametrize("username, password, domain", [
#     (get_test_data()["valid_user"]["username"],
#      get_test_data()["valid_user"]["password"],
#      get_test_data()["valid_user"]["domain"])
# ])
#
# @pytest.mark.parametrize("title1,question1,answer1", [
#     (get_node_creation_data()["Schedule_Callback_Get_Available_Slots"]["NodetemplateTitle"],
#      get_node_creation_data()["Schedule_Callback_Get_Available_Slots"]["nodequestion"],
#      get_node_creation_data()["Schedule_Callback_Get_Available_Slots"]["textcardmsg"])
# ])





@allure.feature("Schedule_Call_Back")
# def test_verify_the_schedule_call_back(page_fixture, username, password,domain, title1, question1, answer1):
def test_verify_the_schedule_call_back(page_fixture):

    username = get_scb_test_data()["valid_user"]["username"]
    password = get_scb_test_data()["valid_user"]["password"]
    domain= get_scb_test_data()["valid_user"]["domain"]

    getAvailableNodeTitle= get_scb_test_data()["Schedule_Callback_Get_Available_Slots"]["NodetemplateTitle"]
    getAvailableNodeQuestion= get_scb_test_data()["Schedule_Callback_Get_Available_Slots"]["nodequestion"]
    getAvailableNodeTextCard= get_scb_test_data()["Schedule_Callback_Get_Available_Slots"]["textcardmsg"]

    newCallBackNodeTitle =  get_scb_test_data()["Schedule_New_CallBack_Request"]["NodetemplateTitle"]
    newCallBackNodeQuestion =  get_scb_test_data()["Schedule_New_CallBack_Request"]["nodequestion"]
    newCallBackNodeTextCard =  get_scb_test_data()["Schedule_New_CallBack_Request"]["textcardmsg"]

    bookingSuccessNodeTitle =  get_scb_test_data()["Booking_Success"]["NodetemplateTitle"]
    bookingSuccessNodeQuestion =  get_scb_test_data()["Booking_Success"]["nodequestion"]
    bookingSuccessNodeTextCard =  get_scb_test_data()["Booking_Success"]["textcardmsg"]

    rescheduleCallBackNodeTitle =  get_scb_test_data()["Reschedule_CallBack_Request"]["NodetemplateTitle"]
    rescheduleCallBackNodeQuestion =  get_scb_test_data()["Reschedule_CallBack_Request"]["nodequestion"]
    rescheduleCallBackNodeTextCard =  get_scb_test_data()["Reschedule_CallBack_Request"]["textcardmsg"]

    issueOccuredNodeTitle =  get_scb_test_data()["Issue_Occured"]["NodetemplateTitle"]
    issueOccuredNodeQuestion =  get_scb_test_data()["Issue_Occured"]["nodequestion"]
    issueOccuredNodeTextCard =  get_scb_test_data()["Issue_Occured"]["textcardmsg"]

    bookingfailedNodeTitle =  get_scb_test_data()["CallBack_Booking_Failed"]["NodetemplateTitle"]
    bookingfailedNodeQuestion =  get_scb_test_data()["CallBack_Booking_Failed"]["nodequestion"]
    bookingfailedNodeTextCard =  get_scb_test_data()["CallBack_Booking_Failed"]["textcardmsg"]

    cancelingCallBackNodeTitle =  get_scb_test_data()["Canceling_CallBack_Request"]["NodetemplateTitle"]
    cancelingCallBackNodeQuestion =  get_scb_test_data()["Canceling_CallBack_Request"]["nodequestion"]
    cancelingCallBackNodeTextCard =  get_scb_test_data()["Canceling_CallBack_Request"]["textcardmsg"]





    """
    Test to verify the 'Schedule Call Back' feature.
    User Request: Customers initiate a callback request through a chatbot, web form, or mobile app.
    Slot Selection: Users can select the earliest available time slot or choose a preferred time.
    Confirmation: The system provides a confirmation message once the request is scheduled.
    Rescheduling & Cancellation: Users can modify or cancel their scheduled callback if needed.
    Agent Assignment: The system assigns an available agent based on business rules and customer priority.
    """

    page = page_fixture  # Playwright page instance

    # Initialize all page objects using a single function
    pages = initialize_page_objects(page)

    with allure.step("Navigating to Login Page"):
        pages["login_page"].navigateToURL()

    with allure.step(f"Logging in as {username}"):
        pages["login_page"].loginDetails(username, domain, password)


    with allure.step(" dasboard page"):
        pages["dashboard_page"].analytics_Page_Validation()
        pages["dashboard_page"].click_central_repository_icon()
    with allure.step(" centralRepo page"):
        pages["centralrepo_page"].click_flowtype_central_repository_icon()


    with allure.step("New Intent Template Inside Flow Repo"):
        pages["flowrepo_page"].navigate_to_new_folder_to_add_new_intent()
        pages["intentTemplate_page"].add_template_name_to_new_intent()
        pages["intent_page"].creating_schedule_callback_scenerio_get_available_slots_node(getAvailableNodeTitle,getAvailableNodeQuestion, getAvailableNodeTextCard)
        pages["intent_page"].creating_schedule_new_callBack_request_node(newCallBackNodeTitle,newCallBackNodeQuestion,newCallBackNodeTextCard)
        pages["intent_page"].creating_booking_success_node(bookingSuccessNodeTitle,bookingSuccessNodeQuestion,bookingSuccessNodeTextCard)
        pages["intent_page"].creating_reschedule_callBack_request_node(rescheduleCallBackNodeTitle,rescheduleCallBackNodeQuestion,rescheduleCallBackNodeTextCard)
        pages["intent_page"].creating_issue_occured_node(issueOccuredNodeTitle,issueOccuredNodeQuestion,issueOccuredNodeTextCard)
        pages["intent_page"].creating_callBack_booking_failed_node(bookingfailedNodeTitle,bookingfailedNodeQuestion,bookingfailedNodeTextCard)
        pages["intent_page"].creating_canceling_callBack_request_node(cancelingCallBackNodeTitle,cancelingCallBackNodeQuestion,cancelingCallBackNodeTextCard)


        # pages["scb"].creating_Schedule_Callback_Get_Available_Slots_Node()
        # pages["scb"].creating_Schedule_New_CallBack_Request_Node()
        # pages["scb"].creating_Booking_Success_Node()
        # pages["scb"].creating_Reschedule_CallBack_Request_Node()
        # pages["scb"].creating_Issue_Occured_Node()
        # pages["scb"].creating_CallBack_Booking_Failed_Node()
        # pages["scb"].creating_Canceling_CallBack_Request_Node()


    with allure.step("Editing Schedule Callback Nodes"):

        # pages["scb_e"].editing_Schedule_Callback_Get_Available_Slots_Node()
        # pages["scb_e"].editing_Schedule_New_CallBack_Request_Node()
        # pages["scb_e"].editing_Booking_Success_Node()
        # pages["scb_e"].editing_Reschedule_CallBack_Request_Node()
        page.pause()
        pages["intent_page"].scb_editing_issue_occurred_node()
        page.pause()
        pages["intent_page"].scb_editing_callBack_booking_failed_node()
        page.pause()


        pages["scb_e"].editing_Canceling_CallBack_Request_Node()

    #
    # with allure.step("Importing the Intent"):
    #     pages["import_intent"].importing_scb_intent()
    #
    # with allure.step("Schedule CallBack Widget"):
    #     pages["widget"].connecting_with_widget()
    #
    # with allure.step("Dashboard"):
    #     pages["dashboard"].dashboard()
