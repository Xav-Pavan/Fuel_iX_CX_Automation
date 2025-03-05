class ScheduleCallBackLocators:
    def __init__(self, page):
        """Constructor to initialize Schedule Call Back locators."""
        self.page = page

        # Navigation Locators

        self.NAVIGATE_CR_NEW_INTENT = self.page.locator("li:nth-child(4) > a")
        self.FLOW_LINK = self.page.get_by_role("link", name="FLOW", exact=True)
        self.FLOW_NEW_JOINE = self.page.get_by_text("Flow_New_Joine")
        self.FLOW_ONE = self.page.get_by_text("one", exact=True)
        self.FLOW_TWO = self.page.get_by_text("2", exact=True)
        self.BTN_CLICK = self.page.get_by_test_id("btn-click")

        # Intent Creation Locators
        self.NEW_INTENT_BUTTON = self.page.get_by_test_id("styl-btn").get_by_text("New Intent")
        self.INTENT_INPUT_BOX = self.page.get_by_test_id("promptinputbox")
        self.INTENT_OK_BUTTON = self.page.get_by_test_id("promptokbutton")
        self.ADD_BTN_FLOW = self.page.get_by_test_id("add-btn-flow")

        # Node Creation Locators
        self.TEMPLATE_TITLE_INPUT = self.page.get_by_placeholder("Enter template title here")
        self.RICH_TEXT_AREA = self.page.locator(".questions-rich-text-area")
        self.ADD_CARDS_BUTTON = self.page.get_by_role("button", name="Add   Cards")
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
        self.RESCHEDULE_FLOW_MENU_ITEM = self.page.locator("(//div[@class='flowMenuItem'][normalize-space()='New Node'])[3]")

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
        self.BOOKING_SUCCESS_NODE = self.page.locator("(//div[@title='Booking_Success'])[1]")
        self.RESCHEDULE_CALLBACK_REQUEST = self.page.locator("(//div[@title='Reschedule_CallBack_Request'])[1]")

        # Node Settings and Actions
        self.NODE_SETTINGS_ICON = self.page.locator("(//img[@class='chatbot-header-icon'])[2]")
        self.ADD_CARDS_BUTTON = self.page.locator("(//button[normalize-space()='Add   Cards'])[1]")
        self.SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")

        # Text Editing Locators
        self.EXISTING_TEXT_FIELD = self.page.locator("(//p[normalize-space()='this is test scb'])[1]")
        self.NEW_TEXT_INPUT = self.page.locator("(//div[@class='ql-editor ql-blank'])[1]")

        # Slot Selection and Mapping
        self.ASK_SLOTS_BUTTON = self.page.locator("(//span[normalize-space()='Ask Slots'])[1]")
        self.ADD_FILTER_ICON_1 = self.page.locator("(//img[@title='Add Filter'])[2]")
        self.ADD_FILTER_ICON_2 = self.page.locator("(//img[@title='Add Filter'])[3]")
        self.SELECT_FIELD_ICON = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]")
        self.SELECT_FIELD_ICON_1 = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[6]")
        self.SELECT_FIELD_ICON_2 = self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]")
        self.SELECT_FIELD_ICON_3 = self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]")
        self.TEXT_INPUT_FIELD = self.page.locator(
            "//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]")
        self.ENTER_KEY = self.page.keyboard.press("Enter")

        # Filtering Options
        self.EMPTY_CONDITION = self.page.locator("//div[normalize-space(text()) ='Empty']")
        self.DONE_BUTTON = self.page.locator("(//button[normalize-space()='Done'])[1]")

        # Question Field and Conditions
        self.QUESTION_FIELD = self.page.locator("(//div[@class='editable-field question-field'])[1]")
        self.TEXT_CONDITION_ICON = self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[4]")
        self.TEXT_CONDITION_ANY = self.page.locator("//div[normalize-space(text()) ='Any']")
        self.MAP_WITH_SLOT_INPUT = self.page.locator(
            "//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]")

        # Button and Webhook Actions
        self.TEXT_RESPONSE_BUTTON = self.page.locator("(//span[normalize-space()='Text'])[1]")
        self.WEBHOOK_BUTTON = self.page.locator("(//span[normalize-space()='Webhook'])[1]")
        self.WEBHOOK_SET_SLOT = self.page.locator("(//div[@class='slot-value-field setSlotField'])[1]")
        self.ADD_SLOT = self.page.locator("(//span[normalize-space()='Add Slot'])[1]")
        self.SET_SLOT_FILED = self.page.locator("(//div[@class='slot-value-field setSlotField'])[2]")
        # Title and Configuration
        self.SELECT_TITLE = self.page.locator("(//div[contains(text(),'Select Title')])[1]")
        self.SELECT_ECB_CALLBACK = self.page.locator(
            "//div[normalize-space(text()) ='ECB schedule callback - Get available slots']")
        self.SEE_MORE_BUTTON = self.page.locator("(//a[normalize-space()='See More'])[1]")
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
        self.ADD_CARDS_BUTTON = self.page.get_by_role("button", name="Add   Cards")
        self.TEXT_OPTION = self.page.get_by_text("Text", exact=True)
        self.GOTO_BUTTON = self.page.locator("(//span[normalize-space()='GoTo'])[1]")
        self.SELECT_DROPDOWN = self.page.locator("(//div[contains(@class,'select__input-container css-19bb58m')])[2]")
        self.SELECT_OPTION = self.page.locator(
            "//div[normalize-space(text()) ='Schedule_Callback_Get_Available_Slots']")

        # Canceling CallBack Request Node Locators
        self.CANCELING_CALLBACK_REQUEST_NODE = self.page.locator("//*[@title='Canceling_CallBack_Request']")
        self.ASK_SLOTS_BUTTON = self.page.get_by_text("Ask Slots", exact=True)
        self.ADD_FILTER_ICON = self.page.locator('//*[@class="add-filter-icon"]//img')
        self.CONDITION_DROPDOWN = self.page.locator('//*[@role="combobox" and @id="Condition"]')
        self.CONDITION_EMPTY = self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Empty']''')
        self.DONE_BUTTON = self.page.locator("//button[normalize-space()='Done']")
        self.QUESTION_FIELD = self.page.locator('//*[@class="editable-field question-field"]')

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
        self.RESPONSE_OPTION = self.page.locator("//a[@id='ddwebhook']")
        self.RESPONSE_VALUE_FIELD = self.page.locator("//input[@placeholder='Value']")
        self.RESPONSE_CONDITION_DROPDOWN = self.page.locator('//*[@role="combobox" and @id="Condition"]')
        self.RESPONSE_CONDITION_EQUALS = self.page.locator(
            '''//*[contains(@id,'listbox')]//descendant::div[text()='Equals']''')

        # Final Save & Exit
        self.FINAL_SAVE_BUTTON = self.page.locator("(//span[normalize-space()='Save'])[1]")
        self.FINAL_BACK_BUTTON = self.page.locator("//button[@class='btn b-other']")

