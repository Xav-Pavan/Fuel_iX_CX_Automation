class IntentTemplatePageLocators:
    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.PROMPT_INPUT_BOX = self.page.get_by_test_id("promptinputbox")
        self.PROMPT_OK_BUTTON = self.page.get_by_test_id("promptokbutton")
        self.NODE_CREATION_PLUS_ICON = self.page.get_by_test_id("add-btn-flow")