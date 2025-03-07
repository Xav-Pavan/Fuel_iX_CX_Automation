class AnalyticsPage:

    def __init__(self, page):
        self.page = page

    def analyticsPageValidation(self):
        self.page.wait_for_url("https://mqa2.xavlab.xyz/analytics")
        assert self.page.url == "https://mqa2.xavlab.xyz/analytics", "Dashboard page URL is incorrect"
        home_page_header = self.page.get_by_text("Analytics & Reports")  # Replace with a unique text or element
        print(home_page_header)
