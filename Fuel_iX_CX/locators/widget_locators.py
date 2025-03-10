class WidgetPageLocators:

    def __init__(self, page):
        """Constructor to initialize login page locators."""
        self.page = page
        self.OPEN_CHAT_BUTTON = self.page.get_by_label("Open Chat")
        self.TRANSACTION_BOT = self.page.locator("//span[@title='Transaction Bot MQA']")
        self.USER_INPUT_MESSAGE = self.page.locator("(//*[@id='user-input-message'])[1]")
        self.SEND_MESSAGE_BUTTON = self.page.locator("(//button[@id='msgSenderButton'])[1]")
        self.NAME_PROMPT = self.page.locator(
            "//span[@class='displayed-text']//b[contains(text(),'So we know who to ask for, what is your name?')]")
        self.PHONE_NUMBER_PROMPT = self.page.locator(
            "//span[@class='displayed-text']//b[contains(text(),'Next, please enter the phone number you want us to')]")
        self.FIRST_AVAILABLE_SLOT = self.page.locator("//ul[@class='list-group']/li[1]")
        self.CALLBACK_CONFIRMATION = self.page.locator(
            "(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[4]")
        self.RESCHEDULE_BUTTON = self.page.locator("(//button[normalize-space()='Reschedule'])[1]")
        self.SECOND_AVAILABLE_SLOT = self.page.locator("//ul[@class='list-group']/li[2]")
        self.RESCHEDULED_CALLBACK_CONFIRMATION = self.page.locator(
            "(//div[@class='rcw-message-text rcw-bot-bubble-radius m-b-5'])[6]")
        self.CANCEL_BUTTON = self.page.locator("(//button[contains(@title,'Cancel')][normalize-space()='Cancel'])[2]")
        self.CLOSE_ICON = self.page.locator("//span[@class='rcw-options-icons cursor close-header']")
        self.SKIP_BUTTON = self.page.locator("(//button[normalize-space()='Skip'])[1]")
        self.CLOSE_BUTTON = self.page.locator("(//button[normalize-space()='Close'])[1]")

