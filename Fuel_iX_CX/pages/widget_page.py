from playwright.sync_api import expect

from Fuel_iX_CX.utils.imports import *


class WidgetPage:

    def __init__(self, page):
        self.page = page

    def openTheWidget(self):
        expect(self.page.get_by_label("Open Chat")).to_be_enabled()
        self.page.get_by_label("Open Chat").click()
        expect(self.page.locator("//span[@title='Transaction Bot MQA']")).to_be_visible()
        self.page.locator("//span[@title='Transaction Bot MQA']").click()
        self.page.get_by_placeholder("Ask me something").fill("Explain all Answer cards in the Chat bot")
        self.page.locator("//button[@id='msgSenderButton']").click()
        time.sleep(3)
        self.page.locator("//span[@class='rcw-options-icons cursor close-header']//img").click()
        self.page.locator("//button[normalize-space()='Skip']").click()
        self.page.locator("//button[normalize-space()='Close']").click()
        time.sleep(3)
        self.page.locator("//span[@title='Refresh Dashboard']").click()
        time.sleep(3)
        print("The Total count of conversion is ",
              self.page.locator("(//h3[@class='report-result'])[1]").text_content())
