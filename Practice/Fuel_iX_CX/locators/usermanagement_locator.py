class UserManagementPageLocators:

    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.DASHBOARDPAGEVALIDATION_TEXT = self.page.locator("//span[@title='Analytics & Reports']")
        self.User_Management_Icon=  self.page.locator("//a[@class='selected']//*[name()='svg']")
        self.Invite_User= self.page.locator("//span[normalize-space()='Invite User']")
        self.Enter_Email = self.page.locator("//input[@placeholder='Enter email id']")
