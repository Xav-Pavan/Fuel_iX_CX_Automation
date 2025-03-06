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

        self.SCB_ISSUE_OCCURED_NODE = self.page.locator("//*[@title='Issue_Occured']")
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
        self.SCB_SLOT_NAME_SELECT_DDOWN = self.page.get_by_role("combobox")

        self.SCB_CONDITION_DROPDOWN = self.page.locator("//*[@role='combobox' and @id='Condition']")
        self.SCB_CONDITION_SELECT_EMPTY_DROPDOWN = self.page.locator("//*[contains(@id,'listbox')]//descendant::div[text()='Empty']")
        self.SCB_DONE_BUTTON = self.page.locator("//button[normalize-space()='Done']")
        self.SCB_PHONE_NUMBER_VALIDATION = self.page.locator(
            "//*[contains(@id,'listbox')]//descendant::div[text()='Phone No.']")
        self.SCB_SELECT_INPUT_FIELD = self.page.locator(
            "//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]")
        self.SCB_WEBHOOK_DROPDOWN = self.page.locator("//*[contains(@id,'wekbook-dropdown')]")
        self.SCB_TIMEZONE_FIELD = self.page.locator("//div[contains(text(),'asia/kolkata')]")
        self.SCB_SERVICE_ID_FIELD = self.page.locator("//div[contains(text(),'1384-e32a1ba4-1287-4698-b82e-3caa902eb131')]")
        self.SCB_SERVICE_NAME_FIELD = self.page.locator("//div[contains(text(),'request-tbs-wls-cb-pcs-sch-cr1-en')]")
        self.SCB_RESPONSE_SCOPE = self.page.locator("//input[@placeholder='Select Scope']")
        self.SCB_RESPONSE_CODE_INPUT = self.page.locator("//input[@placeholder='Value']")
        self.SCB_TEXT_CARD_EDITOR_2 = self.page.locator("//div[@id='quilans5']//div[@class='ql-editor ql-blank']")

