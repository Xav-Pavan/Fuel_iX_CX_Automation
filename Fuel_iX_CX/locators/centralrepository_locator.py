
class CentralRepositoryPageLocators:
    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.FLOW_REPOSITORY_BUTTON= self.page.get_by_role("link", name="FLOW", exact=True)