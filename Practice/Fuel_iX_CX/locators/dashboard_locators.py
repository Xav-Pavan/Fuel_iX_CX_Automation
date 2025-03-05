
class ReportAndAnalyticsDashboardPageLocators:
    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.DASHBOARDPAGEVALIDATION_TEXT = self.page.locator("//span[@title='Analytics & Reports']")
        self.CENTRAL_REPOSITORY_ICON=  self.page.locator("//li[@data-tip='Central Repository']//a")
