class IntentPageLocators:

    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.ADD_CARDS_LINK= self.page.get_by_role("button", name="Add Cards")
        self.TEXT_CARD_BUTTON_ICON= self.page.get_by_text("Text", exact=True)
        self.INPUT_TEXT_TEXT_CARD= self.page.get_by_role("paragraph")
        self.NODE_TEMPLATE_TITLE= self.page.get_by_placeholder("Enter template title here")
        self.NODE_QUESTION= self.page.locator(".questions-rich-text-area")
        self.SAVE_BUTTON= self.page.get_by_role("button", name="Save")
        self.NODE_TEMPLATE_CREATION_SUCCESS_MSG=self.page.locator("//*[@class='MuiAlert-message css-1xsto0d']")
        self.BACK_BUTTON= self.page.get_by_test_id("backbutton-btn")

        ## scb_issue accured node xpath

        self.SCB_ISSUE_OCCURED_NODE = self.page.locator("//*[@title='Issue_Occurred']")
        self.SCB_EDIT_ICON = self.page.locator("//*[@data-action-type='edit']//img[@class='chatbot-header-icon']")
        self.SCB_TEXT_CARD_TEXTBOX = self.page.locator("//div[@class='ql-editor']//p")
        self.SCB_TEXT_BLANK_TEXTBOX = self.page.locator("//div[@class='ql-editor ql-blank']")
        self.SCB_SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")
        self.SCB_BACK_BUTTON = self.page.locator("//button[@class='btn b-other']")


        ## scb_CALLBACK_BOOKING_FAILED_NODE xpath


        self.SCB_CALLBACK_BOOKING_FAILED_NODE = self.page.locator("//*[@title='CallBack_Booking_Failed']")
        self.SCB_ADD_CARDS_BUTTON = self.page.get_by_role("button", name="Add   Cards")
        self.SCB_TEXT_CARD_BUTTON_ICON= self.page.get_by_text("Text", exact=True)
        self.SCB_GOTO_BUTTON = self.page.locator("(//span[normalize-space()='GoTo'])[1]")
        self.SCB_SELECT_GOTO_CONTAINER = self.page.locator("(//div[contains(@class,'select__input-container css-19bb58m')])[2]")
        self.SCB_SCHEDULE_GET_AVAILABLE_SLOTS = self.page.locator("//div[normalize-space(text()) ='Schedule_Callback_Get_Available_Slots']")


        ## scb_CANCELING_CALLBACK_NODE xpath

        self.SCB_CANCELING_CALLBACK_NODE = self.page.locator("//*[@title='Canceling_CallBack_Request']")
        self.SCB_ASK_SLOTS_BUTTON = self.page.get_by_text("Ask Slots", exact=True)
        self.SCB_ADD_FILTER_ICON = self.page.locator("//*[@class='add-filter-icon']//img")
        # self.SCB_SLOT_NAME_SELECT_DDOWN = self.page.get_by_role("combobox")

        self.SCB_CONDITION_DROPDOWN = self.page.locator("//*[@role='combobox' and @id='Condition']")

        self.SCB_CONDITION_SELECT_EMPTY_DROPDOWN = self.page.locator("//*[contains(@id,'listbox')]//descendant::div[text()='Empty']")
        self.SCB_CONDITION_SELECT_EQUALS_DROPDOWN=self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Equals']''')
        self.SCB_CONDITION_SELECT_NOT_EQUALS_DROPDOWN =self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Not Equals']''')

        self.SCB_DONE_BUTTON = self.page.locator("//button[normalize-space()='Done']")

        self.SCB_ASK_SLOT_CARD_TEXTBOX= self.page.locator('//*[@class="editable-field question-field"]')


        self.SCB_PHONE_NUMBER_VALIDATION = self.page.locator(
            "//*[contains(@id,'listbox')]//descendant::div[text()='Phone No.']")
        self.SCB_ASK_SLOT_SAVE_ANSWER_TO_SLOT_DDOWN = self.page.get_by_role("combobox")


        self.SCB_TEXT_CARD_SERVICEID_FILTER_ICON=self.page.locator("(//img[@title='Add Filter'])[3]")
        self.SCB_SLOT_NAME_SELECT_DDOWN_IN_FILTER=self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]")
        self.SCB_SELECT_EMPTY_DDOWN_IN_FILTER= self.page.locator("//div[normalize-space(text()) ='Empty']")
        self.SCB_DONE_BUTTON2 =  self.page.locator("(//button[normalize-space()='Done'])[1]")

        self.SCB_SLOT_NAME_SELECT_DDOWN_FIELD_VALUE = self.page.locator(
            "//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]")
        self.SCB_ADD_WEBHOOK_CARD= self.page.get_by_text("Webhook", exact=True)
        self.SCB_WEBHOOK_DROPDOWN = self.page.locator("//*[contains(@id,'wekbook-dropdown')]")
        self.SCB_CALL_CANCEL_REQUEST_WEBHOOK= self.page.locator("//div[@class='select__option css-1nhws6w-option' and text()='ECB schedule callback - Cancel']")
        self.SCB_TIMEZONE_FIELD = self.page.locator("//div[contains(text(),'asia/kolkata')]")
        self.SCB_EMPTY_WEBHOOK_FIELD=self.page.locator("//div[@class='editable-field']")
        self.SCB_SERVICE_ID_FIELD = self.page.locator("//div[contains(text(),'1384-e32a1ba4-1287-4698-b82e-3caa902eb131')]")
        self.SCB_SERVICE_NAME_FIELD = self.page.locator("//div[contains(text(),'request-tbs-wls-cb-pcs-sch-cr1-en')]")

        self.SCB_SCOPE_DDOWN_IN_FILTER = self.page.locator("//input[@placeholder='Select Scope']")
        self.SCB_WEBHOOK_IN_SCOPE_DDOWN_IN_FILTER= self.page.locator("//a[@id='ddwebhook']")
        self.SCB_SELECT_SR_RESPONSECODE_DDOWN_IN_FILTER=self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]")
        self.SCB_RESPONSE_VALUE_DDOWN_IN_FILTER = self.page.locator("//input[@placeholder='Value']")
        self.SCB_TEXT_CARD_EDITOR_2 = self.page.locator("//div[@id='quilans5']//div[@class='ql-editor ql-blank']")

        # Intent Creation Locators
        self.NEW_INTENT_BUTTON = self.page.get_by_test_id("styl-btn").get_by_text("New Intent")
        self.INTENT_INPUT_BOX = self.page.get_by_test_id("promptinputbox")
        self.INTENT_OK_BUTTON = self.page.get_by_test_id("promptokbutton")
        self.ADD_BTN_FLOW = self.page.get_by_test_id("add-btn-flow")

        # Node Creation Locators
        self.TEMPLATE_TITLE_INPUT = self.page.get_by_placeholder("Enter template title here")
        self.RICH_TEXT_AREA = self.page.locator(".questions-rich-text-area")

        self.TEXT_OPTION = self.page.get_by_text("Text", exact=True)
        self.PRE_DIV_FIRST = self.page.locator("pre div").first
        self.SAVE_BUTTON = self.page.get_by_role("button", name="Save")
        self.BACK_BUTTON = self.page.get_by_test_id("backbutton-btn")

        # Node Success Message Locators
        self.NODE_CREATION_SUCCESS_MESSAGE = self.page.locator("//div[@class='MuiAlert-message css-1xsto0d']")

        # Node Actions
        self.NEW_NODE_CLICK = self.page.locator("//div[@class='rst__rowNodeAdd add-node-uid']")
        self.NEW_NODE_TEXT = self.page.get_by_text("New Node")
        self.NEW_NODE_CLICK_2 = self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[2]")

        # Booking Success Locators
        self.BOOKING_SUCCESS_NODE = self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[2]")
        self.BOOKING_SUCCESS_NEW_NODE = self.page.get_by_text("New Node").nth(1)

        # Reschedule Callback Request Locators
        self.RESCHEDULE_CALLBACK_NODE = self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[3]")
        self.RESCHEDULE_FLOW_MENU_ITEM = self.page.locator(
            "(//div[@class='flowMenuItem'][normalize-space()='New Node'])[3]")

        # Issue Occurred Node Locators
        self.ISSUE_OCCURRED_ADD_BTN_FLOW = self.page.get_by_test_id("add-btn-flow")

        # Callback Booking Failed Node Locators
        self.CALLBACK_BOOKING_FAILED_ADD_BTN_FLOW = self.page.get_by_test_id("add-btn-flow")

        # Canceling Callback Request Locators
        self.CANCELING_CALLBACK_ADD_BTN_FLOW = self.page.get_by_test_id("add-btn-flow")

        # Node Selection Locators
        self.SCHEDULE_CALLBACK_GET_AVAILABLE_SLOTS = self.page.locator(
            "(//div[@title='Schedule_Callback_Get_Available_Slots'])[1]")
        self.SCHEDULE_NEW_CALLBACK_REQUEST = self.page.locator("(//div[@title='Schedule_New_CallBack_Request'])[1]")
        self.TEXT_CARD_CLEAR = self.page.locator("(//p[normalize-space()='submit call back'])[1]")
        self.BOOKING_SUCCESS_NODE_SELECT = self.page.locator("(//div[@title='Booking_Success'])[1]")
        self.RESCHEDULE_CALLBACK_REQUEST = self.page.locator("(//div[@title='Reschedule_CallBack_Request'])[1]")

        # Node Settings and Actions
        self.NODE_SETTINGS_ICON = self.page.locator("(//img[@class='chatbot-header-icon'])[2]")

        self.SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")

        # Text Editing Locators
        self.EXISTING_TEXT_FIELD = self.page.locator("(//p[normalize-space()='this is test scb'])[1]")
        self.NEW_TEXT_INPUT = self.page.locator("(//div[@class='ql-editor ql-blank'])[1]")

        # Slot Selection and Mapping
        self.ASK_SLOTS_BUTTON_1 = self.page.locator("(//span[normalize-space()='Ask Slots'])[1]")
        self.ADD_FILTER_ICON_1 = self.page.locator("(//img[@title='Add Filter'])[2]")
        self.ADD_FILTER_ICON_2 = self.page.locator("(//img[@title='Add Filter'])[3]")
        self.ADD_FILTER_ICON_3 = self.page.locator("(//img[@title='Add Filter'])[4]")
        self.SELECT_FIELD_ICON = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]")
        self.SELECT_FIELD_ICON_1 = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[6]")
        self.SELECT_FIELD_ICON_2 = self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]")
        self.SELECT_FIELD_ICON_3 = self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]")
        self.SELECT_FILED_ICON_4 = self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]")
        self.TEXT_INPUT_FIELD = self.page.locator(
            "//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]")
        self.ENTER_KEY = self.page.keyboard.press("Enter")

        # Filtering Options
        self.EMPTY_CONDITION = self.page.locator("//div[normalize-space(text()) ='Empty']")
        self.DONE_BUTTON_1 = self.page.locator("(//button[normalize-space()='Done'])[1]")

        # Question Field and Conditions
        self.QUESTION_FIELD = self.page.locator("(//div[@class='editable-field question-field'])[1]")
        self.QUESTION_FIELD_2 = self.page.locator("(//div[@class='editable-field question-field'])[2]")
        self.TEXT_CONDITION_ICON = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[4]")
        self.TEXT_CONDITION_ANY = self.page.locator("//div[normalize-space(text()) ='Any']")
        self.MAP_WITH_SLOT_INPUT = self.page.locator(
            "//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]")

        # Button and Webhook Actions
        self.TEXT_RESPONSE_BUTTON = self.page.locator("(//span[normalize-space()='Text'])[1]")
        self.WEBHOOK_BUTTON = self.page.locator("(//span[normalize-space()='Webhook'])[1]")
        self.WEBHOOK_SET_SLOT = self.page.locator("(//div[@class='slot-value-field setSlotField'])[1]")
        self.WEBHOOK_VALUE_CLEAR = self.page.locator("(//div[contains(text(),'desiredTime')])[1]")
        self.FILL_WEBHOOK_VALUE_2 = self.page.locator("(//div[@contenteditable='true'])[13]")
        self.ADD_SLOT = self.page.locator("(//span[normalize-space()='Add Slot'])[1]")
        self.SET_SLOT_FILED = self.page.locator("(//div[@class='slot-value-field setSlotField'])[2]")
        # Title and Configuration
        self.SELECT_TITLE = self.page.locator("(//div[contains(text(),'Select Title')])[1]")
        self.SELECT_ECB_CALLBACK = self.page.locator(
            "//div[normalize-space(text()) ='ECB schedule callback - Get available slots']")
        self.SEE_MORE_BUTTON = self.page.locator("(//a[normalize-space()='See More'])[1]")
        self.SEE_MORE_BUTTON_1 = self.page.locator("(//a[contains(text(),'See More')])[2]")
        self.SEE_MORE_BUTTON_2 = self.page.locator("(//a[contains(text(),'See More')])[1]")
        self.TIME_ZONE_FIELD = self.page.locator("(//div[contains(text(),'asia/kolkata')])[1]")
        self.FILTER_CONDITION = self.page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]")

        # Webhook Response Configuration
        self.WEBHOOK_PHONE_NUMBER_FIELD = self.page.locator("(//div[@contenteditable='true'])[24]")

        # Confirmation Buttons
        self.CONFIRM_BUTTON_1 = self.page.locator("(//button[@class='btn b-other'])[1]")

        # Node Editing Locators
        self.ISSUE_OCCURRED_NODE = self.page.locator("//*[@title='Issue_Occurred']")
        self.EDIT_ICON = self.page.locator("//*[@data-action-type='edit']//img[@class='chatbot-header-icon']")
        self.TEXT_CARD = self.page.locator("//div[@class='ql-editor']//p")
        self.FILL_TEXT_CARD = self.page.locator("//div[@class='ql-editor ql-blank']")
        self.SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")
        self.BACK_BUTTON = self.page.locator("//button[@class='btn b-other']")

        # CallBack Booking Failed Node Locators
        self.CALLBACK_BOOKING_FAILED_NODE = self.page.locator("//*[@title='CallBack_Booking_Failed']")
        self.SELECT_DROPDOWN_4 = self.page.locator("//div[normalize-space(text()) ='CallBack_Booking_Failed']")
        self.ADD_CARDS_BUTTON = self.page.get_by_role("button", name="Add   Cards")

        self.GOTO_BUTTON = self.page.locator("(//span[normalize-space()='GoTo'])[1]")
        self.SELECT_DROPDOWN = self.page.locator("(//div[contains(@class,'select__input-container css-19bb58m')])[2]")
        self.SELECT_DROPDOWN_1 = self.page.locator("(//div[@class='select__input-container css-19bb58m'])[3]")
        self.SELECT_DROPDOWN_3 = self.page.locator("(//div[contains(@class,'select__input-container css-19bb58m')])[4]")
        self.CLICK_WEBHOOK = self.page.locator(
            "//div[normalize-space(text()) ='ECB Schedule Callback - Submit callback']")
        self.FILL_WEBHOOK_VALUE_1 = self.page.locator("(//div[@contenteditable='true'])[7]")
        self.SELECT_OPTION = self.page.locator(
            "//div[normalize-space(text()) ='Schedule_Callback_Get_Available_Slots']")

        # Canceling CallBack Request Node Locators
        self.CANCELING_CALLBACK_REQUEST_NODE = self.page.locator("//*[@title='Canceling_CallBack_Request']")
        self.ASK_SLOTS_BUTTON = self.page.get_by_text("Ask Slots", exact=True)
        self.ADD_FILTER_ICON = self.page.locator('//*[@class="add-filter-icon"]//img')
        self.CONDITION_DROPDOWN = self.page.locator('//*[@role="combobox" and @id="Condition"]')
        self.CONDITION_EMPTY = self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Empty']''')
        self.DONE_BUTTON = self.page.locator("//button[normalize-space()='Done']")

        # Webhook Locators
        self.WEBHOOK_DROPDOWN = self.page.locator("//*[contains(@id,'wekbook-dropdown')]")
        self.WEBHOOK_OPTION = self.page.locator(
            "//div[@class='select__option css-1nhws6w-option' and text()='ECB schedule callback - Cancel']")
        self.TIMEZONE_FIELD = self.page.locator("//div[contains(text(),'asia/kolkata')]")
        self.SERVICE_ID_FIELD = self.page.locator("//div[contains(text(),'1384-e32a1ba4-1287-4698-b82e-3caa902eb131')]")
        self.SERVICE_NAME_FIELD = self.page.locator("//div[contains(text(),'request-tbs-wls-cb-pcs-sch-cr1-en')]")

        # Response Filter Locators
        self.RESPONSE_FILTER_ICON = self.page.locator('//*[@class="add-filter-icon"]//img').nth(4)
        self.RESPONSE_SCOPE = self.page.locator("//input[@placeholder='Select Scope']")
        self.RESPONSE_SCOPE_1 = self.page.locator("(//input[@placeholder='Select Scope'])[1]")
        self.RESPONSE_OPTION = self.page.locator("//a[@id='ddwebhook']")
        self.RESPONSE_VALUE_FIELD = self.page.locator("//input[@placeholder='Value']")
        self.RESPONSE_VALUE_FILED_1 = self.page.locator("(//input[@placeholder='Value'])[1]")
        self.RESPONSE_CONDITION_DROPDOWN = self.page.locator('//*[@role="combobox" and @id="Condition"]')
        self.RESPONSE_CONDITION_EQUALS = self.page.locator(
            '''//*[contains(@id,'listbox')]//descendant::div[text()='Equals']''')

        # Final Save & Exit
        self.FINAL_SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")
        self.FINAL_BACK_BUTTON = self.page.locator("//button[@class='btn b-other']")

        # Node Editing Locators
        self.SCB_1_GET_AVAILABLE_SLOTS_NODE = self.page.locator(
            "(//div[@title='Schedule_Callback_Get_Available_Slots'])[1]")
        self.SCB_1_NODE_SETTINGS_ICON = self.page.locator("(//img[@class='chatbot-header-icon'])[2]")
        self.SCB_1_ADD_CARDS_BUTTON = self.page.locator("(//button[normalize-space()='Add   Cards'])[1]")
        self.SCB_1_EXISTING_TEXT_FIELD = self.page.locator("(//p[normalize-space()='this is test scb'])[1]")
        self.SCB_1_NEW_MESSAGE_FIELD = self.page.locator("(//div[@class='ql-editor ql-blank'])[1]")
        self.SCB_1_ASK_SLOTS_BUTTON = self.page.locator("(//span[normalize-space()='Ask Slots'])[1]")
        self.SCB_1_ADD_FILTER_ICON_2 = self.page.locator("(//img[@title='Add Filter'])[2]")
        self.SCB_1_SELECT_FIELD_DROPDOWN = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]")
        self.SCB_1_SELECT_TEXT_INPUT = self.page.locator(
            "//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]")
        self.SCB_1_TEXT_RESPONSE_FIELD = self.page.locator("(//div[@class='ql-editor ql-blank'])[1]")
        self.SCB_1_PHONE_NUMBER_SELECTION = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[6]")
        self.SCB_1_PHONE_NUMBER_OPTION = self.page.locator("//div[normalize-space(text()) ='Phone No.']")
        self.SCB_1_MAP_WITH_SLOT_INPUT = self.page.locator(
            "//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]")
        self.SCB_1_WEBHOOK_BUTTON = self.page.locator("(//span[normalize-space()='Webhook'])[1]")
        self.SCB_1_WEBHOOK_FILTER_ICON = self.page.locator("(//img[@title='Add Filter'])[5]")
        self.SCB_1_GOTO_BUTTON = self.page.locator("(//span[normalize-space()='GoTo'])[1]")
        self.SCB_1_SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")
        self.SCB_1_CONFIRM_BUTTON = self.page.locator("(//button[@class='btn b-other'])[1]")
        self.SELECT_WEBHOOK_OPTION_1 = self.page.locator(
            "//div[normalize-space(text()) ='Schedule_New_CallBack_Request']")
        self.SCB_1_DONE_BUTTON_1 = self.page.locator("(//button[normalize-space()='Done'])[1]")
        self.SCB_1_EMPTY_CONDITION = self.page.locator("//div[normalize-space(text()) ='Empty']")
        self.EDIT_TEXT_CARD_1 = self.page.locator("(//div[@class='editable-field question-field'])[1]")
        self.CLICKING_OPTION_1 = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[4]")
        self.CLICKING_OPTION_4 = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[8]")
        self.CLICKING_OPTION_2 = self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]")
        self.CLICKING_OPTION_3 = self.page.locator("(//span[normalize-space()='Text'])[1]")
        self.SELECT_TRUE_CONDITION = self.page.locator("(//div[contains(text(),'True')])[1]")
        self.SELECT_FALSE_CONDITION = self.page.locator("//div[normalize-space(text()) ='False']")
        self.SELECT_WEBHOOK_OPTION_2 = self.page.locator(
            "//div[normalize-space(text()) ='ECB schedule callback - Get available slots']")
        self.CLICKING_OPTION_5 = self.page.locator("(//div[@class='editable-field'])[6]")
        self.CLEAR_WEBHOOK_VALUE = self.page.locator(
            "(//div[@class='editable-field'][normalize-space()='phone number'])[1]")
        self.FILL_WEBHOOK_VALUE = self.page.locator("(//div[@contenteditable='true'])[24]")
        self.CLICK_ADD_FILTER = self.page.locator("(//img[contains(@title,'Add Filter')])[6]")
        self.CLICK_ADD_FILTER_1 = self.page.locator("(//img[contains(@title,'Add Filter')])[7]")
        self.SELECT_DROPDOWN_2 = self.page.locator("//div[normalize-space(text()) ='Issue_Occurred']")
        self.FILL_WEBHOOK_VALUE_3 = self.page.locator("(//div[@contenteditable='true'])[17]")
        self.WEBHOOK_DROPDOWN_1 = self.page.locator("//div[normalize-space(text()) ='Booking_Success']")
        self.CLICKING_OPTION_6 = self.page.locator("(//div[@class='select__input-container css-4j0fso'])[1]")
        self.CONDITION_NOT_EQUALS = self.page.locator("//div[normalize-space(text()) ='Not Equals']")
        self.SCB_1_WEBHOOK_BUTTON_1 = self.page.locator("(//a[normalize-space()='webhook'])[1]")
        self.TEXT_CARD_CLEAR_1 = self.page.locator("(//p[normalize-space()='this is booking success'])[1]")
        self.CLICKING_OPTION_7 = self.page.locator("(//span[normalize-space()='Buttons'])[1]")
        self.TEXT_CARD_FILL = self.page.locator("(//div[@class='rich-text-textarea'])[1]")

        # Locators extracted from the provided code
        self.SCB_1_ADD_REPLY_BUTTON = self.page.locator("(//span[@class='blockheadig rightblock addReply'])[1]")
        self.SCB_1_NAME_INPUT = self.page.locator("(//div[@data-placeholder='Name can be changed here'])[1]")
        self.SCB_1_CUSTOM_RADIO_BUTTON = self.page.locator("(//span[@class='custom-radio-btn'])[1]")
        self.SCB_1_DROPDOWN_INDICATOR = self.page.locator(
            "(//div[@class='select__indicator select__dropdown-indicator css-t62vls-indicatorContainer'])[1]")
        self.SCB_1_CANCEL_CALLBACK_OPTION = self.page.locator(
            "//div[normalize-space(text()) ='Canceling_CallBack_Request']")
        self.SCB_1_ADD_BUTTON = self.page.locator("(//button[normalize-space()='Add'])[1]")
        self.SCB_1_QUERY_INPUT = self.page.locator("(//div[@data-placeholder='Enter query'])[1]")
        self.SCB_1_RESCHEDULE_OPTION = self.page.locator(
            "//div[normalize-space(text()) ='Reschedule_CallBack_Request']")
        self.SCB_1_SET_SLOTS_BUTTON = self.page.locator("(//span[normalize-space()='Set Slots'])[1]")
        self.SCB_1_SERVICE_ID_INPUT = self.page.locator("(//div[@class='slot-value-field setSlotField'])[1]")
        self.SCB_1_SERVICE_NAME_INPUT = self.page.locator("(//div[@class='slot-value-field setSlotField'])[2]")
        self.SCB_1_NEW_MESSAGE_FIELD = self.page.locator("(//div[@class='ql-editor ql-blank'])[1]")
        self.SCB_1_SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")
        self.SCB_1_CONFIRM_BUTTON = self.page.locator("(//button[@class='btn b-other'])[1]")
        self.SCB_1_RESCHEDULE_CALLBACK_NODE = self.page.locator("(//div[@title='Reschedule_CallBack_Request'])[1]")
        self.SCB_1_WEBHOOK_BUTTON = self.page.locator("(//span[contains(text(),'Webhook')])[1]")
        self.SCB_1_SEE_MORE_BUTTON = self.page.locator("(//a[contains(text(),'See More')])[1]")
        self.SCB_1_TIMEZONE_FIELD = self.page.locator("(//div[@contenteditable='true'])[9]")
        self.SCB_1_PHONE_NUMBER_FIELD = self.page.locator("(//div[@contenteditable='true'])[20]")
        self.SCB_1_GOTO_BUTTON = self.page.locator("(//span[normalize-space()='GoTo'])[1]")
        self.SCB_1_WEBHOOK_RESPONSE_FIELD = self.page.locator("(//div[contains(text(),'Booking_Success')])[1]")
        self.SCB_1_FALLBACK_RESPONSE_FIELD = self.page.locator(
            "(//div[contains(text(),'CallBack_Booking_Failed')])[1]")
        self.TEXT_CARD_CLEAR_2 = self.page.locator("(//p[normalize-space()='this is reschedule'])[1]")
        self.FILL_WEBHOOK_VALUE_4 = self.page.locator("(//div[@contenteditable='true'])[9]")
        self.FILL_WEBHOOK_VALUE_5 = self.page.locator("(//div[@contenteditable='true'])[20]")
        self.CLICK_WEBHOOK_1 = self.page.locator("//div[normalize-space(text()) ='ECB schedule callback - Reschedule']")

        self.SCB_1_TIME_ZONE_NAME = self.page.locator("(//div[@contenteditable='true'])[25]")
        self.SCB_1_DATE_TIME_FIELD = self.page.locator("(//div[contains(text(),'2021-04-21T12:00:00.000Z')])[1]")
        self.SCB_1_UUID_FIELD = self.page.locator(
            "(//div[contains(text(),'1386-a53e3ab1-ff68-4cb9-ac5f-25edca906154')])[1]")
        self.SCB_1_REQUEST_FIELD = self.page.locator(
            "(//div[contains(text(),'request-tbs-wls-cb-pcs-sch-cr1-en')])[1]")

        # Update slot details
        self.SCB_1_SERVICE_NAME = self.page.locator("(//div[@contenteditable='true'])[30]")
        self.SCB_1_SERVICE_ID = self.page.locator("(//div[@contenteditable='true'])[29]")
        self.SCB_1_SELECTED_SLOT = self.page.locator("(//div[@contenteditable='true'])[28]")

        # Configure Webhook response conditions
        self.SCB_1_ADD_FILTER_BUTTON = self.page.locator("(//img[@title='Add Filter'])[4]")
        self.SCB_1_BOOKING_SUCCESS = self.page.locator("(//div[contains(text(),'Booking_Success')])[1]")
        self.SCB_1_NOT_EQUALS_CONDITION = self.page.locator("(//div[contains(text(),'Not Equals')])[1]")
        self.SCB_1_CALLBACK_BOOKING_FAILED = self.page.locator(
            "(//div[contains(text(),'CallBack_Booking_Failed')])[1]")
        self.SCB_1_DROPDOWN_SELECTION = self.page.locator("(//div[@class='select__input-container css-19bb58m'])[5]")
        self.SCB_1_DROPDOWN_SELECTION_1 = self.page.locator("(//div[@class='react-select-input-width__input-container css-19bb58m'])[1]")


        # import locators
        self.NAVIGATE_CHATBOT_SECTION = self.page.locator("//a[@href='/chat-bot']//*[name()='svg']")
        self.TRANSACTION_BOT_MQA = self.page.get_by_role("heading", name="Transaction Bot MQA")
        self.FLOW_NEW_JOINIEE = self.page.get_by_text("Flow_New_Joinee")
        self.SELECT_IMPORT_NODE = self.page.locator(
            "div:nth-child(12) > .rst__node > .rst__nodeContent > div > .rst__rowWrapper > .rst__row > "
            ".rst__rowContents > .rst__rowTitleRowToolbar > .rst__rowLabel > .rst__rowTitle > div > "
            ".rst__rowTitle__inner"
        )
        self.SELECT_VIRTUOSO_ITEM_LIST = self.page.get_by_test_id("virtuoso-item-list").get_by_text("2")
        self.CHATBOT_ICON_BUTTON_2 = self.page.get_by_test_id("chatbot-icon-btn").locator("img").nth(1)
        self.SELECT_COMMON_TAB = self.page.get_by_text("Common")
        self.SELECT_FLOW_TAB = self.page.get_by_text("FLOW", exact=True)
        self.SELECT_FLOW_NEW_JOINE_IMPORT = self.page.get_by_test_id("import-popup-wrapper").get_by_text(
            "Flow_New_Joine")
        self.SELECT_ONE = self.page.get_by_text("one", exact=True)
        self.SELECT_IMPORT_POPUP_2 = self.page.get_by_test_id("import-popup-wrapper").get_by_text("2", exact=True)
        self.SELECT_FIRST_INTENT = self.page.locator(".intents-list > li").first
        self.IMPORT_BUTTON = self.page.get_by_role("button", name="Import")
        self.IMPORT_SUCCESS_MESSAGE = self.page.locator("//div[@class='MuiAlert-message css-1xsto0d']")
        self.CHATBOT_ICON_BUTTON_1 = self.page.get_by_test_id("chatbot-icon-btn").locator("img").first
        self.TRAIN_JOB_SCHEDULED_MESSAGE = self.page.locator(
            "//div[normalize-space(text()) ='Train job has been scheduled.']")
        self.TRAIN_SUCCESS_MESSAGE = self.page.locator("//div[@class='MuiAlert-message css-1xsto0d']")
        self.TRANSACTION_BOT_TRAINED_MESSAGE = self.page.locator(
            "//div[text()=\"'Transaction Bot MQA' bot trained successfully\"]")
