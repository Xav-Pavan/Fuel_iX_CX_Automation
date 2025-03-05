import time

import pytest

from Fuel_iX_CX.pages.login_page import LoginPage
from Fuel_iX_CX.utils.helpers import get_test_data
from playwright.sync_api import expect, Playwright,Page



@pytest.mark.parametrize("username, password, domain", [
    (get_test_data()["valid_user"]["username"],
     get_test_data()["valid_user"]["password"],
     get_test_data()["valid_user"]["domain"])
])
def test_login_with_valid_credentials(page_fixture, username, password, domain):
    global page
    page = page_fixture  # Using the corrected fixture

    # Login Page
    login_page = LoginPage(page)  # Creating an object for the LoginPage
    login_page.navigateToURL()
    login_page.loginDetails(username, domain, password)
    page.locator("li:nth-child(4) > a").click()
    page.get_by_role("link", name="FLOW", exact=True).click()
    page.get_by_text("Flow_New_Joine").click()
    page.get_by_text("one", exact=True).click()

    page.get_by_text("2", exact=True).click()

    page.get_by_test_id("btn-click").click()

    page.get_by_test_id("styl-btn").get_by_text("New Intent").click()

    page.get_by_test_id("promptinputbox").fill("SCB")

    page.get_by_test_id("promptokbutton").click()

    page.get_by_test_id("add-btn-flow").click()

    page.get_by_placeholder("Enter template title here").fill("get name and phone number")

    page.locator(".questions-rich-text-area").click()

    page.locator(".questions-rich-text-area").fill("this is test scb")

    page.get_by_role("button", name="Add   Cards").click()

    page.get_by_text("Text", exact=True).click()

    page.locator("pre div").first.click()

    page.locator("pre div").first.fill("this is test scb")
    time.sleep(0.5)
    page.get_by_role("button", name="Save").click()
    time.sleep(0.5)
    page.get_by_test_id("backbutton-btn").click()

    page.locator("//div[@class='rst__rowNodeAdd add-node-uid'][1]").click()

    page.get_by_text("New Node").click()

    page.get_by_placeholder("Enter template title here").fill("submit callback")

    page.get_by_role("button", name="Add   Cards").click()

    page.get_by_text("Text", exact=True).click()

    page.get_by_role("paragraph").click()

    page.locator("pre div").first.fill("submit call back")
    time.sleep(0.5)
    page.get_by_role("button", name="Save").click()
    time.sleep(0.5)
    page.get_by_test_id("backbutton-btn").click()

    page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[2]").click()

    page.get_by_text("New Node").nth(1).click()

    page.get_by_placeholder("Enter template title here").fill("booking success")

    page.get_by_role("button", name="Add   Cards").click()

    page.get_by_text("Text", exact=True).click()

    page.get_by_role("paragraph").click()

    page.locator("pre div").first.fill("this is booking sccuess")
    time.sleep(0.5)
    page.get_by_role("button", name="Save").click()
    time.sleep(0.5)
    page.get_by_test_id("backbutton-btn").click()

    page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[3]").click()

    page.locator("(//div[@class='flowMenuItem'][normalize-space()='New Node'])[3]").click()

    page.get_by_placeholder("Enter template title here").fill("reschedule")

    page.get_by_role("button", name="Add   Cards").click()

    page.locator("#react-tabs-13").get_by_test_id("text").locator("i").click()

    page.get_by_role("paragraph").click()

    page.locator("pre div").first.fill("this is reschedule")
    time.sleep(0.5)
    page.get_by_role("button", name="Save").click()
    time.sleep(0.5)
    page.get_by_test_id("backbutton-btn").click()

    page.get_by_test_id("add-btn-flow").click()
    time.sleep(0.5)
    page.get_by_placeholder("Enter template title here").fill("issue occured")
    time.sleep(0.5)
    page.get_by_role("button", name="Add   Cards").click()
    time.sleep(0.5)
    page.get_by_text("Text", exact=True).click()
    time.sleep(0.5)
    page.get_by_role("paragraph").click()
    time.sleep(0.5)
    page.locator("pre div").first.fill("issue occured")
    time.sleep(0.5)
    page.get_by_role("button", name="Save").click()
    time.sleep(0.5)
    page.get_by_test_id("backbutton-btn").click()
    time.sleep(0.5)
    page.get_by_test_id("add-btn-flow").click()
    time.sleep(0.5)
    page.get_by_placeholder("Enter template title here").fill("booking faild")
    time.sleep(0.5)
    page.get_by_role("button", name="Add   Cards").click()
    time.sleep(0.5)

    page.get_by_text("Text", exact=True).click()
    time.sleep(0.5)
    page.get_by_role("paragraph").click()
    time.sleep(0.5)
    page.locator("pre div").first.fill("booking filed")
    time.sleep(0.5)
    page.get_by_role("button", name="Save").click()
    time.sleep(0.5)
    page.get_by_test_id("backbutton-btn").click()
    time.sleep(0.5)
    page.get_by_test_id("add-btn-flow").click()

    page.get_by_placeholder("Enter template title here").fill("cancel")

    page.get_by_text("AUTO REPLYTAGSSelect...").click()

    page.get_by_role("button", name="Add   Cards").click()

    page.get_by_text("Text", exact=True).click()

    page.get_by_role("paragraph").click()
    time.sleep(0.5)
    page.locator("pre div").first.fill("this is cancel")
    time.sleep(0.5)
    page.get_by_role("button", name="Save").click()
    time.sleep(0.5)
    page.get_by_test_id("backbutton-btn").click()
    time.sleep(0.5)


    # # Selecting first node

    page.locator("(//div[@title='get name and phone number'])[1]").click()
    time.sleep(0.5)
    page.locator("(//img[@class='chatbot-header-icon'])[2]").click()
    time.sleep(3)
    page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()
    time.sleep(0.5)
    page.locator("(//p[normalize-space()='this is test scb'])[1]").clear()
    time.sleep(0.5)
    page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("In order to schedule a callback from "
                                                                      "TELUS, we'll need to collect the following"
                                                                      " pieces of info from you:")

    page.locator("(//span[normalize-space()='Ask Slots'])[1]").click()

    page.locator("(//img[@title='Add Filter'])[2]").click()

    page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("name")

    page.keyboard.press("Enter")

    page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]").click()

    page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[6]").click()

    page.locator("//div[normalize-space(text()) ='Empty']").click()

    page.locator("(//button[normalize-space()='Done'])[1]").click()

    page.locator("(//div[@class='editable-field question-field'])[1]").fill("<b>So we know who to ask for, "
                                                                                 "what is your name?</b>")

    page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[4]").click()

    page.locator("//div[normalize-space(text()) ='Any']").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

    page.locator("//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]").fill(
        "name")

    page.keyboard.press("Enter")

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

    page.locator("(//span[normalize-space()='Text'])[1]").click()

    # we need to use dollar symbol for system slots
    page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("Thank you {{$local:name}} ")

    page.locator("(//img[@title='Add Filter'])[3]").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("name")

    page.keyboard.press("Enter")

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

    page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Empty']").click()

    page.locator("(//div[contains(text(),'True')])[1]").click()

    page.locator("//div[normalize-space(text()) ='False']").click()

    page.locator("(//button[normalize-space()='Done'])[1]").click()

    page.locator("(//span[contains(text(),'Ask Slots')])[1]").click()

    page.locator("(//div[@class='editable-field question-field'])[2]").fill("<b>Next, please enter the phone "
                                                                                 "number you want us to call.</b>")

    page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[8]").click()

    page.locator("//div[normalize-space(text()) ='Phone No.']").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

    page.locator("//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]").fill(
        "ph_number")

    page.keyboard.press("Enter")
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

    page.locator("(//span[normalize-space()='Webhook'])[1]").click()

    page.locator("(//img[@title='Add Filter'])[5]").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
        "ph_number")

    page.keyboard.press("Enter")

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

    page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Empty']").click()

    page.locator("(//div[contains(text(),'True')])[1]").click()

    page.locator("//div[normalize-space(text()) ='False']").click()

    page.locator("(//button[normalize-space()='Done'])[1]").click()
    time.sleep(0.5)

    page.locator("(//div[contains(text(),'Select Title')])[1]").click()
    time.sleep(0.5)

    page.locator("//div[normalize-space(text()) ='ECB schedule callback - Get available slots']").click()
    time.sleep(3)
    page.locator("(//a[normalize-space()='See More'])[1]").click()
    time.sleep(0.5)

    page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
    time.sleep(0.5)
    page.locator("(//div[@class='editable-field'])[6]").fill("{{$sys:TimeZoneName}}")
    time.sleep(0.5)
    page.locator("(//a[normalize-space()='See More'])[1]").click()
    time.sleep(0.5)
    page.locator("(//div[@class='editable-field'][normalize-space()='phone number'])[1]").clear()
    time.sleep(0.5)
    page.locator("(//div[@contenteditable='true'])[24]").fill("{{$local:ph_number}}")
    time.sleep(0.5)

    # got to
    page.locator("(//span[normalize-space()='GoTo'])[1]").click()
    time.sleep(0.5)
    page.locator("(//img[@title='Add Filter'])[6]").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("ph_number")

    page.keyboard.press("Enter")

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

    page.locator("(//div[@class='select__input-container css-4j0fso'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Empty']").click()

    page.locator("(//button[normalize-space()='Done'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-19bb58m'])[3]").click()
    time.sleep(0.5)
    page.locator("//div[normalize-space(text()) ='issue occured']").click()
    time.sleep(0.5)

    # 2nd goto
    page.locator("(//span[normalize-space()='GoTo'])[1]").click()
    time.sleep(0.5)
    page.locator("(//img[@title='Add Filter'])[7]").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("ph_number")

    page.keyboard.press("Enter")

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

    page.locator("(//div[@class='select__input-container css-4j0fso'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Empty']").click()

    page.locator("(//div[contains(text(),'True')])[1]").click()

    page.locator("//div[normalize-space(text()) ='False']").click()

    page.locator("(//button[normalize-space()='Done'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-19bb58m'])[4]").click()
    time.sleep(0.5)
    page.locator("//div[normalize-space(text()) ='submit callback']").click()
    time.sleep(0.5)
    page.locator("(//span[normalize-space()='Save'])[1]").click()
    time.sleep(1)
    page.locator("(//button[@class='btn b-other'])[1]").click()
    time.sleep(1)
    page.locator("(//button[@class='btn b-other'])[1]").click()
    time.sleep(1)



    # 2nd node selecting
    page.locator("(//div[@title='submit callback'])[1]").click()
    time.sleep(2)
    page.locator("(//img[@class='chatbot-header-icon'])[2]").click()
    time.sleep(0.5)
    page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()
    page.locator("(//p[normalize-space()='submit call back'])[1]").clear()
    page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("Please wait we are fecting the Agent Info ........")
    page.locator("(//span[normalize-space()='Webhook'])[1]").click()
    page.locator("(//div[@class='select__input-container css-19bb58m'])[2]").click()
    page.locator("//div[normalize-space(text()) ='ECB Schedule Callback - Submit callback']").click()
    time.sleep(2)
    page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
    time.sleep(0.5)
    page.locator("(//div[@contenteditable='true'])[6]").fill("{{$sys:TimeZoneName}}")
    time.sleep(1)
    page.locator("(//a[contains(text(),'See More')])[2]").click()
    page.locator("(//div[contains(text(),'desiredTime')])[1]").clear()
    time.sleep(0.5)
    page.locator("(//div[@contenteditable='true'])[12]").fill("{{$local:selected_slot}}")
    time.sleep(1)
    page.locator("(//div[contains(text(),'phone number')])[1]").clear()
    time.sleep(0.5)
    page.locator("(//div[@contenteditable='true'])[16]").fill("{{$local:ph_number}}")
    time.sleep(1)
    page.locator("(//span[normalize-space()='Text'])[1]").click()
    time.sleep(0.5)
    page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("we are checking the response of the Submit Callback Webhook response is: {{$webhook:sR.responseCode}}  ")
    time.sleep(0.5)
    page.locator("(//span[normalize-space()='GoTo'])[1]").click()
    time.sleep(0.5)
    page.locator("(//img[@title='Add Filter'])[4]").click()
    time.sleep(0.5)
    page.locator("(//input[@placeholder='Select Scope'])[1]").click()
    time.sleep(0.5)
    page.locator("(//a[normalize-space()='webhook'])[1]").click()
    time.sleep(0.5)

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("sR.responseCode")

    page.keyboard.press("Enter")

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
    page.locator("(//input[@placeholder='Value'])[1]").fill("200")


    page.locator("(//button[normalize-space()='Done'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-19bb58m'])[3]").click()
    page.locator("//div[normalize-space(text()) ='booking success']").click()

    page.locator("(//span[normalize-space()='GoTo'])[1]").click()
    page.locator("(//img[@title='Add Filter'])[5]").click()
    page.locator("(//input[@placeholder='Select Scope'])[1]").click()
    page.locator("(//a[normalize-space()='webhook'])[1]").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("sR.responseCode")

    page.keyboard.press("Enter")

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

    page.locator("(//div[@class='select__input-container css-4j0fso'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Not Equals']").click()


    page.locator("(//input[@placeholder='Value'])[1]").fill("200")

    page.locator("(//button[normalize-space()='Done'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-19bb58m'])[4]").click()
    page.locator("//div[normalize-space(text()) ='booking faild']").click()
    page.locator("(//span[normalize-space()='Save'])[1]").click()
    time.sleep(1)
    page.locator("(//button[@class='btn b-other'])[1]").click()
    time.sleep(1)
    page.locator("(//button[@class='btn b-other'])[1]").click()
    time.sleep(1)

    # Selecting 3rd node
    page.locator("(//div[@title='booking success'])[1]").click()
    page.locator("(//img[@class='chatbot-header-icon'])[2]").click()
    page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()
    page.locator("(//p[normalize-space()='this is booking sccuess'])[1]").clear()
    page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("Thanks! An agent will reach out within a half hour of your scheduled time.")

    page.locator("(//span[normalize-space()='Buttons'])[1]").click()
    page.locator("(//div[@class='rich-text-textarea'])[1]").fill("If you want to cancel or reschedule your booking, please click below.")
    page.locator("(//span[@class='blockheadig rightblock addReply'])[1]").click()
    page.locator("(//div[@data-placeholder='Name can be changed here'])[1]").fill("Cancel")
    page.locator("(//span[@class='custom-radio-btn'])[1]").click()
    page.locator("(//div[@class='select__indicator select__dropdown-indicator css-t62vls-indicatorContainer'])[1]").click()
    page.locator("//div[normalize-space(text()) ='cancel']").click()
    time.sleep(1)
    page.locator("(//button[normalize-space()='Add'])[1]").click()

    page.locator("(//span[@class='blockheadig rightblock addReply'])[1]").click()
    page.locator("(//div[@data-placeholder='Name can be changed here'])[1]").fill("No Thanks")
    page.locator("(//div[@data-placeholder='Enter query'])[1]").fill("NeverMind")
    time.sleep(1)
    page.locator("(//button[normalize-space()='Add'])[1]").click()

    page.locator("(//span[@class='blockheadig rightblock addReply'])[1]").click()
    page.locator("(//div[@data-placeholder='Name can be changed here'])[1]").fill("Reschedule")
    page.locator("(//span[@class='custom-radio-btn'])[1]").click()
    page.locator("(//div[@class='select__indicator select__dropdown-indicator css-t62vls-indicatorContainer'])[1]").click()
    page.locator("//div[normalize-space(text()) ='reschedule']").click()
    time.sleep(1)
    page.locator("(//button[normalize-space()='Add'])[1]").click()
    time.sleep(0.5)

    page.locator("(//span[normalize-space()='Set Slots'])[1]").click()
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("serviceId")
    page.keyboard.press("Enter")
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='slot-value-field setSlotField'])[1]").fill("{{$webhook:sR.serviceID}}")
    time.sleep(1)
    page.locator("(//span[normalize-space()='Add Slot'])[1]").click()

    page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
    time.sleep(1)

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("serviceName")
    page.keyboard.press("Enter")
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
    time.sleep(1)
    page.locator("(//div[@class='slot-value-field setSlotField'])[2]").fill("{{$webhook:sR.serviceName}}")
    time.sleep(1)


    page.locator("(//span[normalize-space()='Text'])[1]").click()

    page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("{{$local:serviceId}} , {{$webhook:sR.serviceName}}")

    time.sleep(1)
    page.locator("(//span[normalize-space()='Save'])[1]").click()
    time.sleep(1)
    page.locator("(//button[@class='btn b-other'])[1]").click()
    time.sleep(1)
    page.locator("(//button[@class='btn b-other'])[1]").click()
    time.sleep(1)

    # 4th node creating

    page.locator("(//div[@title='reschedule'])[1]").click()
    page.locator("(//img[@class='chatbot-header-icon'])[2]").click()
    time.sleep(2)
    page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()
    page.locator("(//p[normalize-space()='this is reschedule'])[1]").clear()
    page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("Please wait we are ReScheduling your call back .......")
    page.locator("(//span[normalize-space()='Webhook'])[1]").click()
    page.locator("(//div[@class='select__input-container css-19bb58m'])[2]").click()
    page.locator("//div[normalize-space(text()) ='ECB schedule callback - Get available slots']").click()
    time.sleep(2)
    page.locator("(//a[contains(text(),'See More')])[1]").click()
    page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
    page.locator("(//div[@contenteditable='true'])[8]").fill("{{$sys:TimeZoneName}}")
    page.locator("(//a[normalize-space()='See More'])[1]").click()
    page.locator("(//div[contains(text(),'phone number')])[1]").clear()
    page.locator("(//div[@contenteditable='true'])[19]").fill("{{$local:ph_number}}")
    time.sleep(2)
    page.locator("(//span[contains(text(),'Webhook')])[1]").click()
    time.sleep(2)
    page.locator("(//div[@class='select__input-container css-19bb58m'])[3]").click()
    page.locator("//div[normalize-space(text()) ='ECB schedule callback - Reschedule']").click()
    page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
    page.locator("(//div[@contenteditable='true'])[24]").fill("{{$sys:TimeZoneName}}")
    page.locator("(//div[contains(text(),'2021-04-21T12:00:00.000Z')])[1]").clear()
    page.locator("(//div[contains(text(),'1386-a53e3ab1-ff68-4cb9-ac5f-25edca906154')])[1]").clear()
    page.locator("(//div[contains(text(),'request-tbs-wls-cb-pcs-sch-cr1-en')])[1]").clear()
    page.locator("(//div[@contenteditable='true'])[29]").fill("{{$local:serviceName}}")
    page.locator("(//div[@contenteditable='true'])[28]").fill("{{$local:serviceId}}")
    page.locator("(//div[@contenteditable='true'])[27]").fill("{{$local:selected_slot}}")
    time.sleep(1)
    page.locator("(//span[normalize-space()='GoTo'])[1]").click()
    page.locator("(//img[@title='Add Filter'])[4]").click()
    page.locator("(//input[@placeholder='Select Scope'])[1]").click()
    page.locator("(//a[normalize-space()='webhook'])[1]").click()
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("sR.responseCode")

    page.keyboard.press("Enter")
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
    page.locator("(//input[@placeholder='Value'])[1]").fill("200")

    page.locator("(//button[normalize-space()='Done'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-19bb58m'])[4]").click()
    page.locator("(//div[contains(text(),'booking success')])[1]").click()

    time.sleep(2)
    page.locator("(//span[normalize-space()='GoTo'])[1]").click()
    page.locator("(//img[@title='Add Filter'])[5]").click()
    page.locator("(//input[@placeholder='Select Scope'])[1]").click()
    page.locator("(//a[normalize-space()='webhook'])[1]").click()
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

    page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("sR.responseCode")

    page.keyboard.press("Enter")
    page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
    page.locator("(//div[@class='select__input-container css-4j0fso'])[1]").click()
    page.locator("(//div[contains(text(),'Not Equals')])[1]").click()
    page.locator("(//input[@placeholder='Value'])[1]").fill("200")

    page.locator("(//button[normalize-space()='Done'])[1]").click()
    time.sleep(1)
    page.locator("(//div[@class='select__input-container css-19bb58m'])[5]").click()
    page.locator("(//div[contains(text(),'booking faild')])[1]").click()
    time.sleep(1)
    page.locator("(//span[normalize-space()='Save'])[1]").click()



