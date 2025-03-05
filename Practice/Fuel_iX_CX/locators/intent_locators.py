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


