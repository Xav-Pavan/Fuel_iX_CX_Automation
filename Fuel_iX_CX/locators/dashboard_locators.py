
class ReportAndAnalyticsDashboardPageLocators:
    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.DASHBOARDPAGEVALIDATION_TEXT = self.page.locator("//span[@title='Analytics & Reports']")
        self.CENTRAL_REPOSITORY_ICON=  self.page.locator("//li[@data-tip='Central Repository']//a")


        self.ANALYTICS_REPORTS_TAB = self.page.locator("//li[@data-tip='Analytics and Reports']")
        self.REFRESH_DASHBOARD_BUTTON = self.page.locator(
            "//span[@title='Refresh Dashboard']//img[@class='chatbot-header-icon']")
        self.FIRST_INTERACTIVE_ELEMENT = self.page.locator("(//span[@class='hand'])[1]")
        self.VIEW_TRANSACTIONAL_DETAILS = self.page.locator(
            "(//span[@title='Click to see all transactional details'])[1]")
