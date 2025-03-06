class FlowRepositoryPageLocators:
    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.FLOW_NEW_JOINEE_FOLDER= self.page.get_by_text("Flow_New_Joine")
        self.ONE_SUB_FOLDER= self.page.get_by_text("one", exact=True)
        self.SECOND_SUB_FOLDER=  self.page.get_by_text("2", exact=True)
        self.BTN_CLICK =self.page.get_by_test_id("btn-click")
        self.STYL_BTN_NEW_INTENT =  self.page.get_by_test_id("styl-btn").get_by_text("New Intent")



