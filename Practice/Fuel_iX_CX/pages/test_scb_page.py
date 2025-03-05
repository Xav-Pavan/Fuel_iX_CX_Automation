import time
from playwright.sync_api import expect


class Schedule_Call_Back_Test:

    def __init__(self, page):
        self.page = page

    def schedule_call_back_test(self):
        # self.page.locator("//div[@class='rcw-open-launcher']//*[name()='svg']").click()
        # Click on the required menu item
        self.page.locator("li:nth-child(4) > a").click()
        self.page.get_by_role("link", name="FLOW", exact=True).click()
        self.page.get_by_text("Flow_New_Joine").click()
        self.page.get_by_text("one", exact=True).click()

        # Click on a specific node
        self.page.locator(
            "div:nth-child(55) > .rst__node > .rst__nodeContent > div > "
            ".rst__rowWrapper > .rst__row > .rst__rowContents > "
            ".rst__rowTitleRowToolbar > .rst__rowLabel > .rst__rowTitle > div"
        ).click()

        # Perform button clicks
        self.page.get_by_test_id("btn-click").click()
        self.page.get_by_test_id("styl-btn").get_by_text("New Intent").click()

        # Fill input fields
        self.page.get_by_test_id("promptinputbox").fill("testing123")
        self.page.get_by_test_id("promptokbutton").click()
        self.page.get_by_test_id("add-btn-flow").click()
        self.page.get_by_placeholder("Enter template title here").fill("testing123")

        # Fill the rich text area
        self.page.locator(".questions-rich-text-area").click()
        self.page.locator(".questions-rich-text-area").fill("testing123")

        # Add Cards
        self.page.get_by_role("button", name="Add   Cards").click()
        self.page.locator("(//span[normalize-space()='Text'])[1]").click()

        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("In order to schedule a callback from "
                                                                          "TELUS, we'll need to collect the following"
                                                                          " pieces of info from you:")

        self.page.locator("(//span[normalize-space()='Ask Slots'])[1]").click()

        self.page.locator("(//img[@title='Add Filter'])[2]").click()

        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]").click()

        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("name")

        self.page.keyboard.press("Enter")

        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]").click()

        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[6]").click()

        self.page.locator("//div[normalize-space(text()) ='Empty']").click()

        self.page.locator("(//button[normalize-space()='Done'])[1]").click()

        self.page.locator("(//div[@class='editable-field question-field'])[1]").fill("<b>So we know who to ask for, "
                                                                                     "what is your name?</b>")

        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[4]").click()

        self.page.locator("//div[normalize-space(text()) ='Any']").click()

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

        self.page.locator("//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]").fill(
            "name")

        self.page.keyboard.press("Enter")

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

        self.page.locator("(//span[normalize-space()='Text'])[1]").click()

        # we need to use dollar symbol for system slots
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("Thank you {{$local:name}} ")

        self.page.locator("(//img[@title='Add Filter'])[3]").click()

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("name")

        self.page.keyboard.press("Enter")

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

        self.page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()

        self.page.locator("//div[normalize-space(text()) ='Empty']").click()

        self.page.locator("(//div[contains(text(),'True')])[1]").click()

        self.page.locator("//div[normalize-space(text()) ='False']").click()

        self.page.locator("(//button[normalize-space()='Done'])[1]").click()

        self.page.locator("(//span[contains(text(),'Ask Slots')])[1]").click()

        self.page.locator("(//div[@class='editable-field question-field'])[2]").fill("<b>Next, please enter the phone "
                                                                                     "number you want us to call.</b>")

        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[8]").click()

        self.page.locator("//div[normalize-space(text()) ='Phone No.']").click()

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

        self.page.locator("//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]").fill(
            "ph_number")

        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

        self.page.locator("(//span[normalize-space()='Webhook'])[1]").click()

        self.page.locator("(//img[@title='Add Filter'])[5]").click()

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "ph_number")

        self.page.keyboard.press("Enter")

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

        self.page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()

        self.page.locator("//div[normalize-space(text()) ='Empty']").click()

        self.page.locator("(//div[contains(text(),'True')])[1]").click()

        self.page.locator("//div[normalize-space(text()) ='False']").click()

        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        time.sleep(1)

        self.page.locator("(//div[contains(text(),'Select Title')])[1]").click()
        time.sleep(1)

        self.page.locator("//div[normalize-space(text()) ='ECB schedule callback - Get available slots']").click()
        time.sleep(3)

        self.page.locator("(//a[contains(text(),'See More')])[2]").click()
        time.sleep(2)
        self.page.locator("(//div[@class='editable-field'])[11]").clear()
        time.sleep(2)

        self.page.locator("(//div[@class='editable-field'])[11]").fill("{{$local:ph_number}}")
        time.sleep(2)
        self.page.locator("(//div[@class='editable-field'])[11]").click()

        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        time.sleep(2)

        #Creating new node
        self.page.locator("(//*[name()='svg'][@class='svg-inline--fa fa-arrow-left fa-w-14'])[1]").click()
        time.sleep(2)

        self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[1]").click()
        time.sleep(1)

        self.page.locator("(//div[@class='flowMenuItem'])[1]").click()
        time.sleep(3)

        self.page.locator("(//input[@placeholder='Enter template title here'])[1]").fill("tesing234")
        time.sleep(1)
        self.page.locator("(//div[@class='questions-rich-text-area'])[1]").click()
        self.page.locator("(//div[@class='questions-rich-text-area'])[1]").fill("tesing123 automation")
        self.page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()
        self.page.locator("(//span[normalize-space()='Webhook'])[1]").click()
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[2]").click()
        self.page.locator("//div[normalize-space(text()) ='SHS Submit Callback V1']").click()
        time.sleep(2)
        self.page.locator("(//input[@placeholder='Enter Key'])[5]").fill("timeZoneOffset")
        self.page.locator("(//div[@contenteditable='true'])[6]").fill("{{$sys:TimeZone}}")
        self.page.locator("(//div[@contenteditable='true'])[6]").click()
        time.sleep(1)
        self.page.locator("(//a[normalize-space()='See More'])[1]").click()
        time.sleep(1)

        self.page.locator("(//div[@class='editable-field'])[13]").clear()
        time.sleep(2)

        self.page.locator("(//div[@class='editable-field'])[13]").fill("{{$local:ph_number}}")
        time.sleep(1)
        self.page.locator("(//div[@class='editable-field'])[13]").click()

        time.sleep(1)
        self.page.locator("(//span[normalize-space()='Text'])[1]").click()
        time.sleep(1)
        self.page.locator("(//img[@title='Add Filter'])[2]").click()
        time.sleep(1)
        self.page.locator("(//input[@placeholder='Select Scope'])[1]").click()
        time.sleep(1)
        self.page.locator("(//a[normalize-space()='webhook'])[1]").click()
        time.sleep(1)
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        time.sleep(1)
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "sR.responseCode")
        time.sleep(1)
        self.page.keyboard.press("Enter")
        time.sleep(1)
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        time.sleep(1)
        self.page.locator("(//input[@placeholder='Value'])[1]").fill("200")
        time.sleep(1)
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        time.sleep(1)
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill(
            "Thanks! An agent will reach out within a half hour of your scheduled time.")
        time.sleep(1)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        time.sleep(1)
