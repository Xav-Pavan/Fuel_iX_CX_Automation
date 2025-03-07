import logging
import os
import allure
from playwright.sync_api import expect

from Fuel_iX_CX.data.test_SCB_data import SCB_TestData
from Fuel_iX_CX.locators.intent_locators import IntentPageLocators


class SCBPage:

    def __init__(self, page):
        self.page = page

    def add_text_card(self, text_msg):
        intentlocators.ADD_CARDS_LINK.click()
        intentlocators.TEXT_CARD_BUTTON_ICON.click()
        intentlocators.INPUT_TEXT_TEXT_CARD.fill(text_msg)
        intentlocators.ADD_CARDS_LINK.click()

    def node_creation(self, NodetemplateTitle, nodequestion, textcardmsg):
        ## initializing instance of centralrepository_locator class
        global intentlocators
        intentlocators = IntentPageLocators(self.page)
        self.locators = IntentPageLocators(self.page)

        intentlocators.NODE_TEMPLATE_TITLE.fill(NodetemplateTitle)
        intentlocators.NODE_QUESTION.fill(nodequestion)
        self.add_text_card(textcardmsg)

        # Wait for up to 2 sec
        self.page.wait_for_timeout(500)
        intentlocators.SAVE_BUTTON.wait_for(state="visible", timeout=2000)  # Wait for up to 2 sec
        intentlocators.SAVE_BUTTON.click()

        actual_newnode_sucessmsg = intentlocators.NODE_TEMPLATE_CREATION_SUCCESS_MSG.inner_text()
        Expected__newnode_sucessmsg = "Template Created Successfully."
        assert actual_newnode_sucessmsg == Expected__newnode_sucessmsg, "Assertionfailed"
        print(f"{NodetemplateTitle} is successfully created and validated")

    def creating_schedule_callback_scenerio_get_available_slots_node(self, NodetemplateTitle, nodequestion,
                                                                     textcardmsg):
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_schedule_new_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.locators.NEW_NODE_CLICK.click()
        self.locators.NEW_NODE_TEXT.click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_booking_success_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.locators.NEW_NODE_CLICK_2.click()
        self.locators.BOOKING_SUCCESS_NEW_NODE.click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_reschedule_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.locators.RESCHEDULE_CALLBACK_NODE.click()
        self.locators.RESCHEDULE_FLOW_MENU_ITEM.click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_issue_occured_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.locators.ISSUE_OCCURRED_ADD_BTN_FLOW.click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_callBack_booking_failed_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.locators.ISSUE_OCCURRED_ADD_BTN_FLOW.click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_canceling_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.locators.ISSUE_OCCURRED_ADD_BTN_FLOW.click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def scb_editing_issue_occurred_node(self):
        ##opening issue accured node for editing

        intentlocators.SCB_ISSUE_OCCURED_NODE.click()
        intentlocators.SCB_EDIT_ICON.click()

        # modifying textbox in textcard
        textCardTextBox = intentlocators.SCB_TEXT_CARD_TEXTBOX
        textCardTextBox.scroll_into_view_if_needed()
        textCardTextBox.wait_for(state='visible')
        textCardTextBox.clear()

        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill("I am facing some issues, please try after some time.")

        # saving node and click on back button
        self.page.wait_for_timeout(800)

        intentlocators.SCB_SAVE_BUTTON.click()

        self.page.wait_for_timeout(800)

        intentlocators.SCB_BACK_BUTTON.click()
        self.page.wait_for_timeout(500)

        intentlocators.SCB_BACK_BUTTON.click()

    def scb_editing_callBack_booking_failed_node(self):
        ##opening callBack_booking_failed node for editing

        intentlocators.SCB_CALLBACK_BOOKING_FAILED_NODE.click()
        intentlocators.SCB_EDIT_ICON.click()

        ##modifying text card by clearing text inside textbox
        textCardTextBox = intentlocators.SCB_TEXT_CARD_TEXTBOX
        textCardTextBox.scroll_into_view_if_needed()
        textCardTextBox.wait_for(state='visible')
        textCardTextBox.clear()

        ##modifying text card by inputing values inside textbox
        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill(
            '''Hmm, looks like that time slot is no longer available or you have already booked a time.''')

        ## adding 2 text card in the flow
        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_TEXT_CARD_BUTTON_ICON.click()

        ## input value in textcard textbox
        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill(
            '''Add Card,If you have recently booked a time we will be reaching out within an hour after your scheduled time.''')

        self.page.wait_for_timeout(500)

        ## adding a goto card
        intentlocators.SCB_GOTO_BUTTON.click()

        # clicking on goto after  adding a goto card
        intentlocators.SCB_SELECT_GOTO_CONTAINER.click()

        ## selecting node1 in gotocard
        intentlocators.SCB_SCHEDULE_GET_AVAILABLE_SLOTS.click()

        ## saving node and clicking on back button to move to intent template page
        self.page.wait_for_timeout(800)
        intentlocators.SCB_SAVE_BUTTON.click()

        self.page.wait_for_timeout(800)
        intentlocators.SCB_BACK_BUTTON.click()

        self.page.wait_for_timeout(500)
        intentlocators.SCB_BACK_BUTTON.click()

    def scb_editing_canceling_callBack_request_node(self):
        ## opening canceling_callBack_request_node for editing

        intentlocators.SCB_CANCELING_CALLBACK_NODE.click()
        intentlocators.SCB_EDIT_ICON.click()

        ##modifying text card by clearing text inside textbox
        textCardTextBox = intentlocators.SCB_TEXT_CARD_TEXTBOX
        textCardTextBox.scroll_into_view_if_needed()
        textCardTextBox.wait_for(state='visible')
        textCardTextBox.clear()

        ##modifying text card by inputing values inside textbox
        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill('''Please wait we are Canceling your call back .......''')

        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_ASK_SLOTS_BUTTON.click()

        ## applying filtering inside askslot
        intentlocators.SCB_ADD_FILTER_ICON.nth(1).click()
        ##setting ph_number as slot name inside filter

        self.locators.CLICKING_OPTION_2.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(
            'ph_number')
        self.page.keyboard.press("Enter")

        self.locators.CLICKING_OPTION_2.click()
        self.locators.CLICKING_OPTION_6.click()
        self.locators.SCB_1_EMPTY_CONDITION.click()
        self.locators.SCB_DONE_BUTTON2.click()

        intentlocators.SCB_ASK_SLOT_CARD_TEXTBOX.fill(
            '''<b>Please provide your phone number which you have used while booking your slot.</b>''')

        self.locators.SCB_1_DROPDOWN_SELECTION_1.click()
        intentlocators.SCB_PHONE_NUMBER_VALIDATION.click()

        self.locators.CLICKING_OPTION_2.click()
        self.locators.MAP_WITH_SLOT_INPUT.fill(
            "ph_number")

        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)
        self.locators.CLICKING_OPTION_2.click()
        self.page.wait_for_timeout(500)
        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_ADD_CARDS_BUTTON.click()

        intentlocators.SCB_TEXT_CARD_BUTTON_ICON.click()
        intentlocators.SCB_TEXT_CARD_SERVICEID_FILTER_ICON.click()
        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN_IN_FILTER.click()

        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN_FIELD_VALUE.fill("serviceId")
        self.page.keyboard.press("Enter")

        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN_IN_FILTER.click()
        self.locators.CLICKING_OPTION_6.click()

        # self.page.locator("//div[normalize-space(text()) ='Empty']").click()
        intentlocators.SCB_SELECT_EMPTY_DDOWN_IN_FILTER.click()

        ##clicking on done button in filters
        # self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        intentlocators.SCB_DONE_BUTTON2.click()


        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill('''Sorry, I can't find any callback request.''')
        intentlocators.SCB_ADD_CARDS_BUTTON.click()


        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_ADD_WEBHOOK_CARD.click()


        intentlocators.SCB_WEBHOOK_DROPDOWN.click()
        intentlocators.SCB_CALL_CANCEL_REQUEST_WEBHOOK.click()
        ##setting timezonein webhook card


        intentlocators.SCB_TIMEZONE_FIELD.clear()
        intentlocators.SCB_EMPTY_WEBHOOK_FIELD.nth(3).fill("{{$sys:TimeZoneName}}")


        intentlocators.SCB_SERVICE_ID_FIELD.clear()
        intentlocators.SCB_EMPTY_WEBHOOK_FIELD.nth(6).fill("{{$local:serviceId}}")


        intentlocators.SCB_SERVICE_NAME_FIELD.clear()
        intentlocators.SCB_EMPTY_WEBHOOK_FIELD.nth(7).fill("{{$local:serviceName}}")
        ## click on add cards button
        intentlocators.SCB_ADD_CARDS_BUTTON.click()



        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_TEXT_CARD_BUTTON_ICON.click()


        intentlocators.SCB_ADD_FILTER_ICON.nth(4).click()
        ##apply response=200 in filters inside text card


        intentlocators.SCB_SCOPE_DDOWN_IN_FILTER.click()
        intentlocators.SCB_WEBHOOK_IN_SCOPE_DDOWN_IN_FILTER.click()


        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN_IN_FILTER.click()
        intentlocators.SCB_SELECT_SR_RESPONSECODE_DDOWN_IN_FILTER.fill("sR.responseCode")
        self.page.keyboard.press("Enter")

        # selecting sR.responseCode value=200 in filter

        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN_IN_FILTER.click()
        intentlocators.SCB_CONDITION_DROPDOWN.click()
        intentlocators.SCB_CONDITION_SELECT_EQUALS_DROPDOWN.click()
        intentlocators.SCB_RESPONSE_VALUE_DDOWN_IN_FILTER.fill("200")

        ## click on ok in filter

        intentlocators.SCB_DONE_BUTTON.click()
        self.page.wait_for_timeout(500)

        ## inputing text message in the TEXT card



        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill("Your callback has been cancelled.")
        intentlocators.SCB_ADD_CARDS_BUTTON.click()

        ## adding last  textcard with response!=200


        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_TEXT_CARD_BUTTON_ICON.click()

        ## applying filtering inside text card

        intentlocators.SCB_ADD_FILTER_ICON.nth(5).click()
        ##apply response=200 in filters inside text card


        intentlocators.SCB_SCOPE_DDOWN_IN_FILTER.click()
        intentlocators.SCB_WEBHOOK_IN_SCOPE_DDOWN_IN_FILTER.click()



        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN_IN_FILTER.click()
        intentlocators.SCB_SELECT_SR_RESPONSECODE_DDOWN_IN_FILTER.fill("sR.responseCode")
        self.page.keyboard.press("Enter")


        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN_IN_FILTER.click()
        intentlocators.SCB_CONDITION_DROPDOWN.click()
        intentlocators.SCB_CONDITION_SELECT_NOT_EQUALS_DROPDOWN.click()
        intentlocators.SCB_RESPONSE_VALUE_DDOWN_IN_FILTER.fill("200")
        ##clicking ok button in filter

        intentlocators.SCB_DONE_BUTTON.click()
        # inputing answer in  text card



        intentlocators.SCB_TEXT_CARD_EDITOR_2.fill(
            '''Sorry, We are unable to cancel your callback. Please try after some time.''')


        intentlocators.SCB_ADD_CARDS_BUTTON.click()

        # saving node and click on back button
        self.page.wait_for_timeout(800)


        intentlocators.SCB_SAVE_BUTTON.click()

        self.page.wait_for_timeout(800)

        intentlocators.SCB_BACK_BUTTON.click()
        self.page.wait_for_timeout(500)

        intentlocators.SCB_BACK_BUTTON.click()

    #     adding 4nodes here
    def editing_Schedule_Callback_Get_Available_Slots_Node(self):
        """Modify the 'Get Available Slots' node in the callback schedule."""

        # Select the first node for editing
        self.locators.SCB_1_GET_AVAILABLE_SLOTS_NODE.click()
        self.page.wait_for_timeout(500)
        # Open the node settings
        self.locators.SCB_1_NODE_SETTINGS_ICON.click()
        self.page.wait_for_timeout(500)

        # Add a new card
        self.locators.SCB_1_ADD_CARDS_BUTTON.click()
        self.page.wait_for_timeout(500)

        # Clear the existing text and enter a new message
        self.locators.SCB_1_EXISTING_TEXT_FIELD.clear()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_NEW_MESSAGE_FIELD.fill(SCB_TestData.FIRST_NODE_UPDATE_ANSWER)

        # Ask for user details
        self.locators.SCB_1_ASK_SLOTS_BUTTON.click()
        self.locators.SCB_1_ADD_FILTER_ICON_2.click()

        # Select the required field (e.g., name)
        self.locators.SCB_1_SELECT_FIELD_DROPDOWN.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.CUSTOMER_SLOT_NAME)
        self.page.keyboard.press("Enter")

        # Additional filtering
        self.locators.SCB_1_SELECT_FIELD_DROPDOWN.click()
        self.locators.SCB_1_PHONE_NUMBER_SELECTION.click()
        self.locators.SCB_1_EMPTY_CONDITION.click()
        self.locators.SCB_1_DONE_BUTTON_1.click()

        # Modify the question field to ask for the user's name
        self.locators.EDIT_TEXT_CARD_1.fill(SCB_TestData.ASK_SLOT_ANSWER_1)

        # Set conditions for text input
        self.locators.CLICKING_OPTION_1.click()
        self.locators.TEXT_CONDITION_ANY.click()
        self.locators.CLICKING_OPTION_2.click()
        self.locators.SCB_1_MAP_WITH_SLOT_INPUT.fill(SCB_TestData.CUSTOMER_SLOT_NAME)
        self.page.keyboard.press("Enter")
        self.locators.CLICKING_OPTION_2.click()

        # Add a text response using system slots
        self.locators.CLICKING_OPTION_3.click()

        self.locators.SCB_1_NEW_MESSAGE_FIELD.fill(SCB_TestData.FIRST_NODE_ANSWER_CARD)

        # Add a condition to check if the field is empty
        self.locators.ADD_FILTER_ICON_2.click()
        self.locators.SELECT_FIELD_ICON_3.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.CUSTOMER_SLOT_NAME)
        self.page.keyboard.press("Enter")
        self.locators.SELECT_FIELD_ICON_3.click()
        self.locators.FILTER_CONDITION.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_EMPTY_CONDITION.click()
        self.page.wait_for_timeout(500)
        self.locators.SELECT_TRUE_CONDITION.click()
        self.locators.SELECT_FALSE_CONDITION.click()
        self.locators.SCB_1_DONE_BUTTON_1.click()

        # Ask for phone number
        self.locators.ASK_SLOTS_BUTTON_1.click()
        self.locators.QUESTION_FIELD_2.fill(SCB_TestData.ASK_SLOT_ANSWER_2)
        self.locators.CLICKING_OPTION_4.click()
        self.locators.SCB_1_PHONE_NUMBER_OPTION.click()

        # Map phone number slot
        self.locators.SELECT_FIELD_ICON_3.click()
        self.locators.SCB_1_MAP_WITH_SLOT_INPUT.fill(SCB_TestData.CUSTOMER_SLOT_PHONE_NUMBER)
        self.page.keyboard.press("Enter")
        self.locators.SELECT_FIELD_ICON_3.click()

        # Add webhook
        self.locators.SCB_1_WEBHOOK_BUTTON.click()
        self.locators.SCB_1_WEBHOOK_FILTER_ICON.click()
        self.locators.SELECT_FILED_ICON_4.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.CUSTOMER_SLOT_PHONE_NUMBER)
        self.page.keyboard.press("Enter")
        self.locators.SELECT_FILED_ICON_4.click()

        # Apply conditions to webhook response
        self.locators.FILTER_CONDITION.click()
        self.locators.SCB_1_EMPTY_CONDITION.click()
        self.locators.SELECT_TRUE_CONDITION.click()
        self.locators.SELECT_FALSE_CONDITION.click()
        self.locators.SCB_1_DONE_BUTTON_1.click()
        self.page.wait_for_timeout(500)

        # Set a title for the node
        self.locators.SELECT_TITLE.click()
        self.locators.SELECT_WEBHOOK_OPTION_2.click()

        # Configure additional settings
        self.locators.SEE_MORE_BUTTON.click()
        self.locators.TIMEZONE_FIELD.clear()
        self.locators.CLICKING_OPTION_5.fill(SCB_TestData.WEBHOOK_TIME_ZONE)

        self.locators.SEE_MORE_BUTTON.click()
        self.locators.CLEAR_WEBHOOK_VALUE.clear()

        self.locators.FILL_WEBHOOK_VALUE.fill(SCB_TestData.WEBHOOK_PHONE_NUMBER)

        self.locators.SCB_1_GOTO_BUTTON.click()
        self.page.wait_for_timeout(500)

        self.locators.CLICK_ADD_FILTER.click()
        self.locators.SELECT_FILED_ICON_4.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.CUSTOMER_SLOT_PHONE_NUMBER)
        self.page.keyboard.press("Enter")
        self.locators.SELECT_FILED_ICON_4.click()

        # Apply conditions to webhook response
        self.locators.FILTER_CONDITION.click()
        self.locators.SCB_1_EMPTY_CONDITION.click()
        self.locators.SCB_1_DONE_BUTTON_1.click()
        self.page.wait_for_timeout(500)

        self.locators.SELECT_DROPDOWN_1.click()
        self.locators.SELECT_DROPDOWN_2.click()

        self.locators.SCB_1_GOTO_BUTTON.click()
        self.page.wait_for_timeout(500)

        self.locators.CLICK_ADD_FILTER_1.click()
        self.locators.SELECT_FILED_ICON_4.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.CUSTOMER_SLOT_PHONE_NUMBER)
        self.page.keyboard.press("Enter")
        self.locators.SELECT_FILED_ICON_4.click()

        # Apply conditions to webhook response
        self.locators.FILTER_CONDITION.click()
        self.locators.SCB_1_EMPTY_CONDITION.click()
        self.locators.SELECT_TRUE_CONDITION.click()
        self.locators.SELECT_FALSE_CONDITION.click()
        self.locators.SCB_1_DONE_BUTTON_1.click()
        self.page.wait_for_timeout(500)

        self.locators.SELECT_DROPDOWN_3.click()
        self.locators.SELECT_WEBHOOK_OPTION_1.click()

        # Save changes
        self.page.wait_for_timeout(800)
        self.locators.SCB_1_SAVE_BUTTON.click()
        self.page.wait_for_timeout(800)

        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)

        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)

    @allure.step("Editing 'Schedule New CallBack Request' Node")
    def editing_Schedule_New_CallBack_Request_Node(self):
        """Modify the 'Schedule New CallBack Request' node in the callback schedule."""

        # Select the second node for editing
        self.locators.SCHEDULE_NEW_CALLBACK_REQUEST.click()
        self.page.wait_for_timeout(500)

        # Open the node settings
        self.locators.SCB_1_NODE_SETTINGS_ICON.click()
        self.page.wait_for_timeout(500)

        # Add a new card to the node
        self.locators.SCB_1_ADD_CARDS_BUTTON.click()

        # Clear existing text and update with a new message
        self.locators.TEXT_CARD_CLEAR.clear()
        self.locators.SCB_1_NEW_MESSAGE_FIELD.fill(SCB_TestData.SECOND_ANSWER_CARD)

        # Add a Webhook action
        self.locators.SCB_1_WEBHOOK_BUTTON.click()
        self.locators.SELECT_DROPDOWN.click()
        self.locators.CLICK_WEBHOOK.click()
        self.page.wait_for_timeout(500)

        # Modify timezone information
        self.locators.TIMEZONE_FIELD.clear()
        self.page.wait_for_timeout(500)
        self.locators.FILL_WEBHOOK_VALUE_1.fill(SCB_TestData.WEBHOOK_TIME_ZONE)
        self.page.wait_for_timeout(500)

        # Expand advanced settings
        self.locators.SEE_MORE_BUTTON_1.click()

        # Modify the desired callback time
        self.locators.WEBHOOK_VALUE_CLEAR.clear()
        self.page.wait_for_timeout(500)
        self.locators.FILL_WEBHOOK_VALUE_2.fill(SCB_TestData.WEBHOOK_SELECTED_SLOT)
        self.page.wait_for_timeout(500)

        # Modify phone number details
        self.locators.CLEAR_WEBHOOK_VALUE.clear()
        self.page.wait_for_timeout(500)
        self.locators.FILL_WEBHOOK_VALUE_3.fill(SCB_TestData.WEBHOOK_PHONE_NUMBER)
        self.page.wait_for_timeout(500)

        # Add a text message to display the webhook response
        self.locators.CLICKING_OPTION_3.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_NEW_MESSAGE_FIELD.fill(SCB_TestData.SECOND_ANSWER_CARD_2)
        self.page.wait_for_timeout(500)

        # Configure 'GoTo' logic based on Webhook response
        self.locators.GOTO_BUTTON.click()
        self.page.wait_for_timeout(500)
        self.locators.ADD_FILTER_ICON_3.click()
        self.page.wait_for_timeout(500)

        # Select 'Webhook' scope

        self.locators.RESPONSE_SCOPE_1.click()

        self.locators.SCB_1_WEBHOOK_BUTTON_1.click()

        # Apply conditions for webhook response
        self.locators.CLICKING_OPTION_2.click()

        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.WEBHOOK_RESPONSE)

        self.page.keyboard.press("Enter")
        self.locators.CLICKING_OPTION_2.click()
        self.locators.RESPONSE_VALUE_FILED_1.fill(SCB_TestData.STATUS_CODE)
        self.locators.SCB_1_DONE_BUTTON_1.click()
        self.page.wait_for_timeout(500)

        # Navigate to 'Booking Success' if Webhook response is successful
        self.locators.SELECT_DROPDOWN_1.click()
        self.locators.WEBHOOK_DROPDOWN_1.click()

        # Configure fallback logic when Webhook response is not 200
        self.locators.SCB_1_GOTO_BUTTON.click()

        self.locators.SCB_1_WEBHOOK_FILTER_ICON.click()
        self.locators.RESPONSE_SCOPE.click()
        self.locators.SCB_1_WEBHOOK_BUTTON_1.click()

        self.locators.CLICKING_OPTION_2.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.WEBHOOK_RESPONSE)
        self.page.keyboard.press("Enter")

        # Modify condition to check for unsuccessful response
        self.locators.CLICKING_OPTION_2.click()
        self.locators.CLICKING_OPTION_6.click()
        self.locators.CONDITION_NOT_EQUALS.click()
        self.locators.RESPONSE_VALUE_FILED_1.fill(SCB_TestData.STATUS_CODE)

        # Confirm fallback navigation to 'CallBack_Booking_Failed'
        self.locators.SCB_1_DONE_BUTTON_1.click()
        self.page.wait_for_timeout(500)
        self.locators.SELECT_DROPDOWN_3.click()
        self.locators.SELECT_DROPDOWN_4.click()

        # Save changes
        self.page.wait_for_timeout(1000)
        self.locators.SCB_1_SAVE_BUTTON.click()
        self.page.wait_for_timeout(1000)

        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)

    @allure.step("Editing 'Booking Success' Node")
    def editing_Booking_Success_Node(self):
        """Modify the 'Booking Success' node in the callback schedule."""

        # Select the third node for editing
        self.locators.BOOKING_SUCCESS_NODE_SELECT.click()

        # Open the node settings
        self.locators.SCB_1_NODE_SETTINGS_ICON.click()

        # Add a new card to the node
        self.locators.SCB_1_ADD_CARDS_BUTTON.click()
        self.page.wait_for_timeout(500)
        # Clear the existing message and update with a new one
        self.locators.TEXT_CARD_CLEAR_1.clear()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_NEW_MESSAGE_FIELD.fill(SCB_TestData.THIRD_NODE_ANSWER_2)

        # Add button options for cancellation and rescheduling
        self.locators.CLICKING_OPTION_7.click()
        self.locators.TEXT_CARD_FILL.fill(SCB_TestData.THIRD_NODE_ANSWER_3)

        # Add 'Cancel' button with navigation to 'Canceling_CallBack_Request'
        self.locators.SCB_1_ADD_REPLY_BUTTON.click()
        self.locators.SCB_1_NAME_INPUT.fill(SCB_TestData.CANCEL_BUTTON)
        self.locators.SCB_1_CUSTOM_RADIO_BUTTON.click()
        self.locators.SCB_1_DROPDOWN_INDICATOR.click()
        self.locators.SCB_1_CANCEL_CALLBACK_OPTION.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_ADD_BUTTON.click()

        # Add 'No Thanks' button with a custom query
        self.locators.SCB_1_ADD_REPLY_BUTTON.click()
        self.locators.SCB_1_NAME_INPUT.fill(SCB_TestData.NO_THANKS_BUTTON)
        self.locators.SCB_1_QUERY_INPUT.fill(SCB_TestData.NO_THANKS_BUTTON_MESSAGE)
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_ADD_BUTTON.click()

        # Add 'Reschedule' button with navigation to 'Reschedule_CallBack_Request'
        self.locators.SCB_1_ADD_REPLY_BUTTON.click()
        self.locators.SCB_1_NAME_INPUT.fill(SCB_TestData.RESCHEDULE_BUTTON)
        self.locators.SCB_1_CUSTOM_RADIO_BUTTON.click()
        self.locators.SCB_1_DROPDOWN_INDICATOR.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_RESCHEDULE_OPTION.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_ADD_BUTTON.click()
        self.page.wait_for_timeout(500)

        # Configure slots for the webhook response
        self.locators.SCB_1_SET_SLOTS_BUTTON.click()

        # Set 'serviceId' slot from webhook response
        self.locators.CLICKING_OPTION_2.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(
            "serviceId")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)
        self.locators.CLICKING_OPTION_2.click()
        self.page.wait_for_timeout(500)
        self.locators.CLICKING_OPTION_2.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_SERVICE_ID_INPUT.fill(SCB_TestData.WEBHOOK_SERVICE_ID)
        self.page.wait_for_timeout(500)
        self.locators.ADD_SLOT.click()

        # Set 'serviceName' slot from webhook response
        self.locators.SELECT_FIELD_ICON_3.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.SERVICE_NAME_SLOT)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)
        self.locators.SELECT_FIELD_ICON_3.click()
        self.page.wait_for_timeout(500)
        self.locators.SELECT_FIELD_ICON_3.click()
        self.page.wait_for_timeout(500)
        self.locators.SET_SLOT_FILED.fill(SCB_TestData.WEBHOOK_SERVICE_NAME)
        self.page.wait_for_timeout(500)

        # Add a text message displaying the collected slot values
        self.locators.CLICKING_OPTION_3.click()
        self.locators.SCB_1_NEW_MESSAGE_FIELD.fill(SCB_TestData.THIRD_NODE_ANSWER_4)

        # Save changes and exit the editor
        self.page.wait_for_timeout(800)
        self.locators.SCB_1_SAVE_BUTTON.click()
        self.page.wait_for_timeout(800)
        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)

    @allure.step("Editing 'Reschedule CallBack Request' Node")
    def editing_Reschedule_CallBack_Request_Node(self):
        """Modify the 'Reschedule CallBack Request' node in the callback schedule."""

        # Select the fourth node for editing
        self.locators.RESCHEDULE_CALLBACK_REQUEST.click()

        # Open the node settings
        self.locators.SCB_1_NODE_SETTINGS_ICON.click()
        self.page.wait_for_timeout(500)

        # Add a new card to the node
        self.locators.SCB_1_ADD_CARDS_BUTTON.click()

        # Clear the existing message and update with a new one
        self.locators.TEXT_CARD_CLEAR_2.clear()
        self.locators.SCB_1_NEW_MESSAGE_FIELD.fill(SCB_TestData.FOURTH_NODE_ANSWER_2)

        # Add a Webhook action for getting available slots
        self.locators.SCB_1_WEBHOOK_BUTTON.click()
        self.locators.SELECT_DROPDOWN.click()
        self.locators.SELECT_WEBHOOK_OPTION_2.click()
        self.page.wait_for_timeout(500)

        # Expand advanced settings
        self.locators.SEE_MORE_BUTTON_2.click()

        # Modify timezone information
        self.locators.TIMEZONE_FIELD.clear()
        self.locators.FILL_WEBHOOK_VALUE_4.fill(SCB_TestData.WEBHOOK_TIME_ZONE)

        # Modify phone number details
        self.locators.SEE_MORE_BUTTON.click()
        self.locators.CLEAR_WEBHOOK_VALUE.clear()
        self.locators.FILL_WEBHOOK_VALUE_5.fill(SCB_TestData.WEBHOOK_PHONE_NUMBER)
        self.page.wait_for_timeout(500)

        # Add another Webhook action for rescheduling
        self.locators.SCB_1_WEBHOOK_BUTTON.click()
        self.page.wait_for_timeout(500)
        self.locators.SELECT_DROPDOWN_1.click()
        self.locators.CLICK_WEBHOOK_1.click()

        # Modify timezone and clear unnecessary fields
        self.locators.TIMEZONE_FIELD.clear()
        self.locators.SCB_1_TIME_ZONE_NAME.fill(SCB_TestData.WEBHOOK_TIME_ZONE)
        self.locators.SCB_1_DATE_TIME_FIELD.clear()
        self.locators.SCB_1_UUID_FIELD.clear()
        self.locators.SCB_1_REQUEST_FIELD.clear()

        # Update slot details
        self.locators.SCB_1_SERVICE_NAME.fill(SCB_TestData.LOCAL_SERVICE_NAME)
        self.locators.SCB_1_SERVICE_ID.fill(SCB_TestData.LOCAL_SERVICE_ID)
        self.locators.SCB_1_SELECTED_SLOT.fill(SCB_TestData.WEBHOOK_SELECTED_SLOT)
        self.page.wait_for_timeout(500)

        # Configure 'GoTo' logic for successful rescheduling
        self.locators.GOTO_BUTTON.click()
        self.locators.SCB_1_ADD_FILTER_BUTTON.click()
        self.locators.RESPONSE_SCOPE_1.click()
        self.locators.SCB_1_WEBHOOK_BUTTON_1.click()

        # Apply conditions for webhook response
        self.locators.CLICKING_OPTION_2.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.WEBHOOK_RESPONSE)
        self.page.keyboard.press("Enter")
        self.locators.CLICKING_OPTION_2.click()
        self.locators.RESPONSE_VALUE_FILED_1.fill(SCB_TestData.STATUS_CODE)

        self.locators.SCB_1_DONE_BUTTON_1.click()
        self.page.wait_for_timeout(500)

        # Navigate to 'Booking Success' if Webhook response is successful
        self.locators.SELECT_DROPDOWN_3.click()
        self.locators.SCB_1_BOOKING_SUCCESS.click()

        self.page.wait_for_timeout(500)

        # Configure fallback logic when Webhook response is not 200
        self.locators.GOTO_BUTTON.click()
        self.locators.SCB_1_WEBHOOK_FILTER_ICON.click()
        self.locators.RESPONSE_SCOPE_1.click()
        self.locators.SCB_1_WEBHOOK_BUTTON_1.click()

        self.locators.SELECT_FIELD_ICON_2.click()
        self.locators.SCB_1_SELECT_TEXT_INPUT.fill(SCB_TestData.WEBHOOK_RESPONSE)
        self.page.keyboard.press("Enter")

        # Modify condition to check for unsuccessful response
        self.locators.CLICKING_OPTION_2.click()
        self.locators.CLICKING_OPTION_6.click()
        self.locators.SCB_1_NOT_EQUALS_CONDITION.click()
        self.locators.RESPONSE_VALUE_FILED_1.fill(SCB_TestData.STATUS_CODE)

        # Confirm fallback navigation to 'CallBack_Booking_Failed'
        self.locators.SCB_1_DONE_BUTTON_1.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_DROPDOWN_SELECTION.click()
        self.locators.SCB_1_CALLBACK_BOOKING_FAILED.click()

        # Save changes and exit the editor
        self.page.wait_for_timeout(800)
        self.locators.SCB_1_SAVE_BUTTON.click()
        self.page.wait_for_timeout(800)
        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)
        self.locators.SCB_1_CONFIRM_BUTTON.click()
        self.page.wait_for_timeout(500)

    # import
    @allure.step("Importing BA_Schedule_call_back_Scenario Intent")
    def importing_scb_intent(self):
        """Method to navigate and import the SCB intent into the chatbot flow."""
        with allure.step("Navigating to Flow Section"):
            logging.info("🤖 Navigating to the Chatbot section...")
            self.locators.NAVIGATE_CHATBOT_SECTION.click()
            self.locators.TRANSACTION_BOT_MQA.click()

        with allure.step("Selecting Flow_New_Joinee"):
            self.locators.FLOW_NEW_JOINIEE.click()

        with allure.step("Selecting a node for Import"):
            self.locators.SELECT_IMPORT_NODE.click()

        with allure.step("Selecting elements for import"):
            self.locators.SELECT_VIRTUOSO_ITEM_LIST.click()
            self.locators.CHATBOT_ICON_BUTTON_2.click()
            self.locators.SELECT_COMMON_TAB.click()
            self.locators.SELECT_FLOW_TAB.click()

        with allure.step("Selecting Flow_New_Joine for import"):
            self.locators.SELECT_FLOW_NEW_JOINE_IMPORT.click()
            self.locators.SELECT_ONE.click()
            self.locators.SELECT_IMPORT_POPUP_2.click()

        with allure.step("Selecting first intent from the list"):
            self.locators.SELECT_FIRST_INTENT.click()

        with allure.step("Clicking on Import Button"):
            logging.info("📥 Importing the newly created intent...")
            self.locators.IMPORT_BUTTON.click()
            Import_successfully = self.locators.IMPORT_SUCCESS_MESSAGE.inner_text()
            print(Import_successfully)
            assert Import_successfully == "Templates imported successfully in bot category."
            screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, "Import_successfully.png")
            self.page.screenshot(path=screenshot_path)

            print(f"Screenshot saved at: {screenshot_path}")

        with allure.step("Train the Bot"):
            self.locators.CHATBOT_ICON_BUTTON_1.click()
            expect(self.locators.TRAIN_JOB_SCHEDULED_MESSAGE).to_be_visible(
                timeout=50000)
            Train_successfully = self.locators.TRAIN_SUCCESS_MESSAGE.inner_text()
            print(Train_successfully)
            assert Train_successfully == "Train job has been scheduled."
            screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, "Train_job_has_been_scheduled.png")

            self.page.screenshot(path=screenshot_path)

        with allure.step("Verifying success message after bot training"):
            expect(self.locators.TRANSACTION_BOT_TRAINED_MESSAGE) \
                .to_be_visible(timeout=50000)
            Trained_successfully = self.locators.TRAIN_SUCCESS_MESSAGE.inner_text()
            print(Trained_successfully)
            assert Trained_successfully == "'Transaction Bot MQA' bot trained successfully"
            screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH,
                                           "Transaction_Bot_MQA_bot_trained_successfully.png")

            self.page.screenshot(path=screenshot_path)

    @allure.step("Connecting with the widget and scheduling a call back")
    def connecting_with_widget(self):
        """Automates the chat interaction for scheduling a call back using the widget."""

        # Step 1: Open Chat Widget
        logging.info("💬 Launching the widget...")
        expect(self.page.get_by_label("Open Chat")).to_be_enabled()
        self.page.get_by_label("Open Chat").click()

        # Step 2: Select the 'Transaction Bot MQA'
        expect(self.page.locator("//span[@title='Transaction Bot MQA']")).to_be_visible()
        self.page.locator("//span[@title='Transaction Bot MQA']").click()
        # Waiting for the bot to load

        # Step 3: Request for the earliest possible time slot
        expect(self.page.locator("(//*[@id='user-input-message'])[1]")).to_be_visible(timeout=50000)
        self.page.locator("(//*[@id='user-input-message'])[1]").fill(SCB_TestData.FIRST_NODE_QUESTION)
        self.page.locator("(//button[@id='msgSenderButton'])[1]").click()

        # Step 4: Provide user name (e.g., Hulk)

        expect(self.page.locator(
            "//span[@class='displayed-text']//b[contains(text(),'So we know who to ask for, what is your name?')]")).to_be_visible(
            timeout=60000)
        self.page.locator("(//*[@id='user-input-message'])[1]").fill("Hulk")
        expect(self.page.locator("(//button[@id='msgSenderButton'])[1]")).to_be_enabled(timeout=50000)
        self.page.locator("(//button[@id='msgSenderButton'])[1]").click()

        # Step 5: Provide phone number

        expect(self.page.locator(
            "//span[@class='displayed-text']//b[contains(text(),'Next, please enter the phone number you want us to')]")).to_be_visible(
            timeout=60000)
        self.page.locator("(//*[@id='user-input-message'])[1]").fill("9172736951")
        expect(self.page.locator("(//button[@id='msgSenderButton'])[1]")).to_be_enabled(timeout=50000)
        self.page.locator("(//button[@id='msgSenderButton'])[1]").click()

        # Step 6: Select the first available callback slot
        expect(self.page.locator("//ul[@class='list-group']/li[1]")).to_be_visible(timeout=60000)
        self.page.locator("//ul[@class='list-group']/li[1]").click()

        # Step 7: Extract and print the callback confirmation message
        expect(self.page.locator("(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[4]")).to_be_visible(
            timeout=50000)
        callback_value = self.page.locator(
            "(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[4]").inner_text()
        print(f"Initial Callback Confirmation: {callback_value}")

        # Step 8: Click 'Reschedule' button
        expect(self.page.locator("(//button[normalize-space()='Reschedule'])[1]")).to_be_visible(timeout=60000)
        self.page.locator("(//button[normalize-space()='Reschedule'])[1]").click()

        # Step 9: Select the second available callback slot
        expect(self.page.locator("//ul[@class='list-group']/li[2]")).to_be_visible(timeout=60000)
        self.page.locator("//ul[@class='list-group']/li[2]").click()

        # Step 10: Extract and print the rescheduled callback confirmation message
        expect(self.page.locator("(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[6]")).to_be_visible(
            timeout=50000)
        next_callback_value = self.page.locator(
            "(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[6]").inner_text()
        print(f"Rescheduled Callback Confirmation: {next_callback_value}")

        # Step 11: Cancel the scheduled callback
        expect(self.page.locator("(//button[contains(@title,'Cancel')][normalize-space()='Cancel'])[2]")).to_be_visible(
            timeout=60000)
        self.page.locator("(//button[contains(@title,'Cancel')][normalize-space()='Cancel'])[2]").click()

        # Step 12: Click on the cross icon options
        expect(self.page.locator("//span[@class='rcw-options-icons cursor close-header']")).to_be_visible(
            timeout=50000)
        self.page.locator("//span[@class='rcw-options-icons cursor close-header']").click()

        # Step 13: Skip feedback and close the widget
        expect(self.page.locator("(//button[normalize-space()='Skip'])[1]")).to_be_visible(timeout=60000)
        self.page.locator("(//button[normalize-space()='Skip'])[1]").click()
        expect(self.page.locator("(//button[normalize-space()='Close'])[1]")).to_be_enabled(timeout=60000)
        self.page.locator("(//button[normalize-space()='Close'])[1]").click()

    def dashboard(self):
        """Automates the navigation and interaction with the dashboard."""

        # Step 1: Click on 'Analytics and Reports' section
        self.page.locator("//li[@data-tip='Analytics and Reports']").click()

        # Step 2: Click on the 'Refresh Dashboard' button
        expect(
            self.page.locator("//span[@title='Refresh Dashboard']//img[@class='chatbot-header-icon']")).to_be_visible(
            timeout=60000)
        self.page.locator("//span[@title='Refresh Dashboard']//img[@class='chatbot-header-icon']").click()

        # Step 3: Click on the first interactive element in the dashboard
        expect(self.page.locator("(//span[@class='hand'])[1]")).to_be_visible(timeout=50000)
        self.page.locator("(//span[@class='hand'])[1]").click()

        # Step 4: Click to expand and view all transactional details
        expect(self.page.locator("(//span[@title='Click to see all transactional details'])[1]")).to_be_visible(
            timeout=50000)
        self.page.locator("(//span[@title='Click to see all transactional details'])[1]").click()

        # Step 5: Capture a full-page screenshot for verification
        # screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH)
        # self.page.screenshot(path=screenshot_path, full_page=True)
        # allure.attach.file(screenshot_path, name="Dashboard Screenshot", attachment_type=allure.attachment_type.PNG)
        # Ensure the directory exists
        os.makedirs(SCB_TestData.SCREENSHOT_PATH, exist_ok=True)

        # Define the full screenshot path
        screenshot_filename = "dashboard_screenshot"
        screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, f"{screenshot_filename}{SCB_TestData.FILE_TYPE}")

        # Capture screenshot
        self.page.screenshot(path=screenshot_path, full_page=True)

        # Attach screenshot to Allure report
        allure.attach.file(screenshot_path, name="Dashboard Screenshot", attachment_type=allure.attachment_type.PNG)
