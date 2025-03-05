from Fuel_iX_CX.utils.imports import *


class Schedule_Call_Back:
    """Class to handle the editing of Schedule Call Back nodes in the Playwright UI."""

    def __init__(self, page):
        """Initialize the class with a Playwright page instance."""
        self.page = page

    @allure.step("Editing 'Schedule Callback Get Available Slots' Node")
    def editing_Schedule_Callback_Get_Available_Slots_Node(self):
        """Modify the 'Get Available Slots' node in the callback schedule."""

        # Select the first node for editing
        self.page.locator("(//div[@title='Schedule_Callback_Get_Available_Slots'])[1]").click()
        self.page.wait_for_timeout(500)
        # Open the node settings
        self.page.locator("(//img[@class='chatbot-header-icon'])[2]").click()
        self.page.wait_for_timeout(500)

        # Add a new card
        self.page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()
        self.page.wait_for_timeout(500)

        # Clear the existing text and enter a new message
        self.page.locator("(//p[normalize-space()='this is test scb'])[1]").clear()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill(
            "In order to schedule a callback from TELUS, we'll need to collect the following pieces of info from you:"
        )

        # Ask for user details
        self.page.locator("(//span[normalize-space()='Ask Slots'])[1]").click()
        self.page.locator("(//img[@title='Add Filter'])[2]").click()

        # Select the required field (e.g., name)
        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("name")
        self.page.keyboard.press("Enter")

        # Additional filtering
        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[5]").click()
        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[6]").click()
        self.page.locator("//div[normalize-space(text()) ='Empty']").click()
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()

        # Modify the question field to ask for the user's name
        self.page.locator("(//div[@class='editable-field question-field'])[1]").fill(
            "<b>So we know who to ask for, what is your name?</b>"
        )

        # Set conditions for text input
        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[4]").click()
        self.page.locator("//div[normalize-space(text()) ='Any']").click()
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]").fill(
            "name")
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()

        # Add a text response using system slots
        self.page.locator("(//span[normalize-space()='Text'])[1]").click()

        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill("Thank you {{$local:name}} ")

        # Add a condition to check if the field is empty
        self.page.locator("(//img[@title='Add Filter'])[3]").click()
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("name")
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
        self.page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("//div[normalize-space(text()) ='Empty']").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[contains(text(),'True')])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='False']").click()
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()

        # Ask for phone number
        self.page.locator("(//span[contains(text(),'Ask Slots')])[1]").click()
        self.page.locator("(//div[@class='editable-field question-field'])[2]").fill(
            "<b>Next, please enter the phone number you want us to call.</b>"
        )
        self.page.locator("(//*[name()='svg'][@class='css-8mmkcg'])[8]").click()
        self.page.locator("//div[normalize-space(text()) ='Phone No.']").click()

        # Map phone number slot
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
        self.page.locator("//div[normalize-space(text())='Map with slot']//following::input[@type='text'][1]").fill(
            "ph_number"
        )
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()

        # Add webhook
        self.page.locator("(//span[normalize-space()='Webhook'])[1]").click()
        self.page.locator("(//img[@title='Add Filter'])[5]").click()
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "ph_number"
        )
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

        # Apply conditions to webhook response
        self.page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Empty']").click()
        self.page.locator("(//div[contains(text(),'True')])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='False']").click()
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        self.page.wait_for_timeout(500)

        # Set a title for the node
        self.page.locator("(//div[contains(text(),'Select Title')])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='ECB schedule callback - Get available slots']").click()

        # Configure additional settings
        self.page.locator("(//a[normalize-space()='See More'])[1]").click()
        self.page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
        self.page.locator("(//div[@class='editable-field'])[6]").fill("{{$sys:TimeZoneName}}")

        self.page.locator("(//a[normalize-space()='See More'])[1]").click()
        self.page.locator("(//div[@class='editable-field'][normalize-space()='phone number'])[1]").clear()

        self.page.locator("(//div[@contenteditable='true'])[24]").fill("{{$local:ph_number}}")

        self.page.locator("(//span[normalize-space()='GoTo'])[1]").click()
        self.page.wait_for_timeout(500)

        self.page.locator("(//img[contains(@title,'Add Filter')])[6]").click()
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "ph_number"
        )
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

        # Apply conditions to webhook response
        self.page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Empty']").click()
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        self.page.wait_for_timeout(500)

        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[3]").click()
        self.page.locator("//div[normalize-space(text()) ='Issue_Occured']").click()

        self.page.locator("(//span[normalize-space()='GoTo'])[1]").click()
        self.page.wait_for_timeout(500)

        self.page.locator("(//img[contains(@title,'Add Filter')])[7]").click()
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "ph_number"
        )
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[3]").click()

        # Apply conditions to webhook response
        self.page.locator("(//div[@class='filter-dropdown css-b62m3t-container'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Empty']").click()
        self.page.locator("(//div[contains(text(),'True')])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='False']").click()
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        self.page.wait_for_timeout(500)

        self.page.locator("(//div[contains(@class,'select__input-container css-19bb58m')])[4]").click()
        self.page.locator("//div[normalize-space(text()) ='Schedule_New_CallBack_Request']").click()

        # Save changes
        self.page.wait_for_timeout(1000)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        self.page.wait_for_timeout(1000)

        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)

        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)

    @allure.step("Editing 'Schedule New CallBack Request' Node")
    def editing_Schedule_New_CallBack_Request_Node(self):
        """Modify the 'Schedule New CallBack Request' node in the callback schedule."""

        # Select the second node for editing
        self.page.locator("(//div[@title='Schedule_New_CallBack_Request'])[1]").click()
        self.page.wait_for_timeout(500)

        # Open the node settings
        self.page.locator("(//img[@class='chatbot-header-icon'])[2]").click()
        self.page.wait_for_timeout(500)

        # Add a new card to the node
        self.page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()

        # Clear existing text and update with a new message
        self.page.locator("(//p[normalize-space()='submit call back'])[1]").clear()
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill(
            "Please wait, we are fetching the Agent Info..."
        )

        # Add a Webhook action
        self.page.locator("(//span[normalize-space()='Webhook'])[1]").click()
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[2]").click()
        self.page.locator("//div[normalize-space(text()) ='ECB Schedule Callback - Submit callback']").click()
        self.page.wait_for_timeout(500)

        # Modify timezone information
        self.page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@contenteditable='true'])[6]").fill("{{$sys:TimeZoneName}}")
        self.page.wait_for_timeout(500)

        # Expand advanced settings
        self.page.locator("(//a[contains(text(),'See More')])[2]").click()

        # Modify the desired callback time
        self.page.locator("(//div[contains(text(),'desiredTime')])[1]").clear()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@contenteditable='true'])[12]").fill("{{$local:selected_slot}}")
        self.page.wait_for_timeout(500)

        # Modify phone number details
        self.page.locator("(//div[contains(text(),'phone number')])[1]").clear()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@contenteditable='true'])[16]").fill("{{$local:Set 'serviceName' slot from webhook response}}")
        self.page.wait_for_timeout(500)

        # Add a text message to display the webhook response
        self.page.locator("(//span[normalize-space()='Text'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill(
            "Checking the response of the booking success. Webhook response: {{$webhook:sR.responseCode}}"
        )
        self.page.wait_for_timeout(500)

        # Configure 'GoTo' logic based on Webhook response
        self.page.locator("(//span[normalize-space()='GoTo'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//img[@title='Add Filter'])[4]").click()
        self.page.wait_for_timeout(500)

        # Select 'Webhook' scope
        self.page.locator("(//input[@placeholder='Select Scope'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//a[normalize-space()='webhook'])[1]").click()
        self.page.wait_for_timeout(500)

        # Apply conditions for webhook response
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "sR.responseCode"
        )
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("(//input[@placeholder='Value'])[1]").fill("200")
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        self.page.wait_for_timeout(500)

        # Navigate to 'Booking Success' if Webhook response is successful
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[3]").click()
        self.page.locator("//div[normalize-space(text()) ='Booking_Success']").click()

        # Configure fallback logic when Webhook response is not 200
        self.page.locator("(//span[normalize-space()='GoTo'])[1]").click()
        self.page.locator("(//img[@title='Add Filter'])[5]").click()
        self.page.locator("(//input[@placeholder='Select Scope'])[1]").click()
        self.page.locator("(//a[normalize-space()='webhook'])[1]").click()

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "sR.responseCode"
        )
        self.page.keyboard.press("Enter")

        # Modify condition to check for unsuccessful response
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("(//div[@class='select__input-container css-4j0fso'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Not Equals']").click()
        self.page.locator("(//input[@placeholder='Value'])[1]").fill("200")

        # Confirm fallback navigation to 'CallBack_Booking_Failed'
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[4]").click()
        self.page.locator("//div[normalize-space(text()) ='CallBack_Booking_Failed']").click()

        # Save changes
        self.page.wait_for_timeout(800)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        self.page.wait_for_timeout(800)

        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)

    @allure.step("Editing 'Booking Success' Node")
    def editing_Booking_Success_Node(self):
        """Modify the 'Booking Success' node in the callback schedule."""

        # Select the third node for editing
        self.page.locator("(//div[@title='Booking_Success'])[1]").click()

        # Open the node settings
        self.page.locator("(//img[@class='chatbot-header-icon'])[2]").click()

        # Add a new card to the node
        self.page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()
        self.page.wait_for_timeout(500)
        # Clear the existing message and update with a new one
        self.page.locator("(//p[normalize-space()='this is booking success'])[1]").clear()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill(
            "Thanks! An agent will contact you at your scheduled time to assist you."
        )

        # Add button options for cancellation and rescheduling
        self.page.locator("(//span[normalize-space()='Buttons'])[1]").click()
        self.page.locator("(//div[@class='rich-text-textarea'])[1]").fill(
            "If you want to cancel or reschedule your booking, please click below."
        )

        # Add 'Cancel' button with navigation to 'Canceling_CallBack_Request'
        self.page.locator("(//span[@class='blockheadig rightblock addReply'])[1]").click()
        self.page.locator("(//div[@data-placeholder='Name can be changed here'])[1]").fill("Cancel")
        self.page.locator("(//span[@class='custom-radio-btn'])[1]").click()
        self.page.locator(
            "(//div[@class='select__indicator select__dropdown-indicator css-t62vls-indicatorContainer'])[1]"
        ).click()
        self.page.locator("//div[normalize-space(text()) ='Canceling_CallBack_Request']").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//button[normalize-space()='Add'])[1]").click()

        # Add 'No Thanks' button with a custom query
        self.page.locator("(//span[@class='blockheadig rightblock addReply'])[1]").click()
        self.page.locator("(//div[@data-placeholder='Name can be changed here'])[1]").fill("No Thanks")
        self.page.locator("(//div[@data-placeholder='Enter query'])[1]").fill("NeverMind")
        self.page.wait_for_timeout(500)
        self.page.locator("(//button[normalize-space()='Add'])[1]").click()

        # Add 'Reschedule' button with navigation to 'Reschedule_CallBack_Request'
        self.page.locator("(//span[@class='blockheadig rightblock addReply'])[1]").click()
        self.page.locator("(//div[@data-placeholder='Name can be changed here'])[1]").fill("Reschedule")
        self.page.locator("(//span[@class='custom-radio-btn'])[1]").click()
        self.page.locator(
            "(//div[@class='select__indicator select__dropdown-indicator css-t62vls-indicatorContainer'])[1]"
        ).click()
        self.page.wait_for_timeout(500)
        self.page.locator("//div[normalize-space(text()) ='Reschedule_CallBack_Request']").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//button[normalize-space()='Add'])[1]").click()
        self.page.wait_for_timeout(500)

        # Configure slots for the webhook response
        self.page.locator("(//span[normalize-space()='Set Slots'])[1]").click()

        # Set 'serviceId' slot from webhook response
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "serviceId")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='slot-value-field setSlotField'])[1]").fill("{{$webhook:sR.serviceID}}")
        self.page.wait_for_timeout(500)
        self.page.locator("(//span[normalize-space()='Add Slot'])[1]").click()

        # Set 'serviceName' slot from webhook response
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(            "serviceName")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[2]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='slot-value-field setSlotField'])[2]").fill("{{$webhook:sR.serviceName}}")
        self.page.wait_for_timeout(500)

        # Add a text message displaying the collected slot values
        self.page.locator("(//span[normalize-space()='Text'])[1]").click()
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill(
            " Your service details are as follows: Service ID:{{$local:serviceId}} ,and Service Name:{service_name}")

        # Save changes and exit the editor
        self.page.wait_for_timeout(800)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        self.page.wait_for_timeout(800)
        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)

    @allure.step("Editing 'Reschedule CallBack Request' Node")
    def editing_Reschedule_CallBack_Request_Node(self):
        """Modify the 'Reschedule CallBack Request' node in the callback schedule."""

        # Select the fourth node for editing
        self.page.locator("(//div[@title='Reschedule_CallBack_Request'])[1]").click()

        # Open the node settings
        self.page.locator("(//img[@class='chatbot-header-icon'])[2]").click()
        self.page.wait_for_timeout(500)

        # Add a new card to the node
        self.page.locator("(//button[normalize-space()='Add   Cards'])[1]").click()

        # Clear the existing message and update with a new one
        self.page.locator("(//p[normalize-space()='this is reschedule'])[1]").clear()
        self.page.locator("(//div[@class='ql-editor ql-blank'])[1]").fill(
            "Please wait, we are rescheduling your call back..."
        )

        # Add a Webhook action for getting available slots
        self.page.locator("(//span[normalize-space()='Webhook'])[1]").click()
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[2]").click()
        self.page.locator("//div[normalize-space(text()) ='ECB schedule callback - Get available slots']").click()
        self.page.wait_for_timeout(500)

        # Expand advanced settings
        self.page.locator("(//a[contains(text(),'See More')])[1]").click()

        # Modify timezone information
        self.page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
        self.page.locator("(//div[@contenteditable='true'])[8]").fill("{{$sys:TimeZoneName}}")

        # Modify phone number details
        self.page.locator("(//a[normalize-space()='See More'])[1]").click()
        self.page.locator("(//div[contains(text(),'phone number')])[1]").clear()
        self.page.locator("(//div[@contenteditable='true'])[19]").fill("{{$local:ph_number}}")
        self.page.wait_for_timeout(500)

        # Add another Webhook action for rescheduling
        self.page.locator("(//span[contains(text(),'Webhook')])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[3]").click()
        self.page.locator("//div[normalize-space(text()) ='ECB schedule callback - Reschedule']").click()

        # Modify timezone and clear unnecessary fields
        self.page.locator("(//div[contains(text(),'asia/kolkata')])[1]").clear()
        self.page.locator("(//div[@contenteditable='true'])[24]").fill("{{$sys:TimeZoneName}}")
        self.page.locator("(//div[contains(text(),'2021-04-21T12:00:00.000Z')])[1]").clear()
        self.page.locator("(//div[contains(text(),'1386-a53e3ab1-ff68-4cb9-ac5f-25edca906154')])[1]").clear()
        self.page.locator("(//div[contains(text(),'request-tbs-wls-cb-pcs-sch-cr1-en')])[1]").clear()

        # Update slot details
        self.page.locator("(//div[@contenteditable='true'])[29]").fill("{{$local:serviceName}}")
        self.page.locator("(//div[@contenteditable='true'])[28]").fill("{{$local:serviceId}}")
        self.page.locator("(//div[@contenteditable='true'])[27]").fill("{{$local:selected_slot}}")
        self.page.wait_for_timeout(500)

        # Configure 'GoTo' logic for successful rescheduling
        self.page.locator("(//span[normalize-space()='GoTo'])[1]").click()
        self.page.locator("(//img[@title='Add Filter'])[4]").click()
        self.page.locator("(//input[@placeholder='Select Scope'])[1]").click()
        self.page.locator("(//a[normalize-space()='webhook'])[1]").click()

        # Apply conditions for webhook response
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "sR.responseCode"
        )
        self.page.keyboard.press("Enter")
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("(//input[@placeholder='Value'])[1]").fill("200")

        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        self.page.wait_for_timeout(500)

        # Navigate to 'Booking Success' if Webhook response is successful
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[4]").click()
        self.page.locator("(//div[contains(text(),'Booking_Success')])[1]").click()

        self.page.wait_for_timeout(500)

        # Configure fallback logic when Webhook response is not 200
        self.page.locator("(//span[normalize-space()='GoTo'])[1]").click()
        self.page.locator("(//img[@title='Add Filter'])[5]").click()
        self.page.locator("(//input[@placeholder='Select Scope'])[1]").click()
        self.page.locator("(//a[normalize-space()='webhook'])[1]").click()

        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "sR.responseCode"
        )
        self.page.keyboard.press("Enter")

        # Modify condition to check for unsuccessful response
        self.page.locator("(//div[@class='select__input-container css-1duuv5x'])[1]").click()
        self.page.locator("(//div[@class='select__input-container css-4j0fso'])[1]").click()
        self.page.locator("(//div[contains(text(),'Not Equals')])[1]").click()
        self.page.locator("(//input[@placeholder='Value'])[1]").fill("200")

        # Confirm fallback navigation to 'CallBack_Booking_Failed'
        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//div[@class='select__input-container css-19bb58m'])[5]").click()
        self.page.locator("(//div[contains(text(),'CallBack_Booking_Failed')])[1]").click()

        # Save changes and exit the editor
        self.page.wait_for_timeout(800)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        self.page.wait_for_timeout(800)
        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)
        self.page.locator("(//button[@class='btn b-other'])[1]").click()
        self.page.wait_for_timeout(500)

    @allure.step("Editing 'Issue_Occurred' Node")
    def editing_Issue_Occurred_Node(self):
        self.page.locator("//*[@title='Issue_Occured']").click()

        self.page.locator("//*[@data-action-type='edit']//img[@class='chatbot-header-icon']").click()

        textcardwebele = self.page.locator("//div[@class='ql-editor']//p")
        textcardwebele.scroll_into_view_if_needed()
        textcardwebele.wait_for(state='visible')
        textcardwebele.clear()
        self.page.locator("//div[@class='ql-editor ql-blank']").fill(
            "I am facing some issues, please try after some time.")

        # saving node and click on back button
        self.page.wait_for_timeout(800)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        self.page.wait_for_timeout(800)
        self.page.locator("//button[@class='btn b-other']").click()
        self.page.wait_for_timeout(500)
        self.page.locator("//button[@class='btn b-other']").click()

    @allure.step("CallBack_Booking_Failed' Node")
    def editing_CallBack_Booking_Failed_Node(self):
        self.page.locator("//*[@title='CallBack_Booking_Failed']").click()

        self.page.locator("//*[@data-action-type='edit']//img[@class='chatbot-header-icon']").click()
        ##modifying 1text cards
        textcardwebele = self.page.locator("//div[@class='ql-editor']//p")
        textcardwebele.scroll_into_view_if_needed()
        textcardwebele.wait_for(state='visible')
        textcardwebele.clear()
        self.page.locator("//div[@class='ql-editor ql-blank']").fill(
            '''Hmm, looks like that time slot is no longer available or you have already booked a time.''')

        ## add 2 text card

        self.page.get_by_role("button", name="Add   Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        self.page.locator("//div[@class='ql-editor ql-blank']").fill(
            '''Add Card,If you have recently booked a time we will be reaching out within an hour after your scheduled time. ''')
        self.page.wait_for_timeout(500)
        self.page.locator("(//span[normalize-space()='GoTo'])[1]").click()
        self.page.locator("(//div[contains(@class,'select__input-container css-19bb58m')])[2]").click()
        self.page.locator("//div[normalize-space(text()) ='Schedule_Callback_Get_Available_Slots']").click()

        # # add a button card
        # self.page.get_by_role("button", name="Add   Cards").click()
        # self.page.get_by_text("Buttons", exact=True).click()
        # self.page.locator("//*[@class='rich-text-textarea']").fill('''Otherwise, the slot may now be full. Please click "Schedule callback" below to select another time slot.''')
        # self.page.locator("//*[@class='blockheadig rightblock addReply']").click()
        # self.page.get_by_test_id("configure-quick-reply").locator("div").filter(has_text="Button Title").locator("div").nth(2).fill("Schedule_Callback_Get_Available_Slots")
        # self.page.locator("//*[@type='radio' and @value='goto']").click()
        #
        # self.page.locator("(//div[@class='select__indicator select__dropdown-indicator css-t62vls-indicatorContainer'])[1]").click()
        # ## this value is static once card title change ,this needs changing
        # time.sleep(2)
        # self.page.locator("//*[normalize-space(text()) ='Schedule_Callback_Get_Available_Slots']").hover().click()
        # self.page.get_by_test_id("configure-quick-reply").get_by_role("button", name="Add").click()
        # self.page.get_by_role("button", name="Add   Cards").click()
        # ## saving node and click on back button
        self.page.wait_for_timeout(800)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        self.page.wait_for_timeout(800)
        self.page.locator("//button[@class='btn b-other']").click()
        self.page.wait_for_timeout(500)
        self.page.locator("//button[@class='btn b-other']").click()

    @allure.step("Canceling CallBack Request' Node")
    def editing_Canceling_CallBack_Request_Node(self):
        self.page.locator("//*[@title='Canceling_CallBack_Request']").click()

        self.page.locator("//*[@data-action-type='edit']//img[@class='chatbot-header-icon']").click()

        # adding first text card in node
        textcardwebele = self.page.locator("//div[@class='ql-editor']//p")
        textcardwebele.scroll_into_view_if_needed()
        textcardwebele.wait_for(state='visible')
        textcardwebele.clear()
        self.page.locator("//div[@class='ql-editor ql-blank']").fill(
            '''Please wait we are Canceling your call back .......''')

        # adding 2 ask slot with filter ph_number empty true
        self.page.get_by_role("button", name="Add Cards").click()
        self.page.get_by_text("Ask Slots", exact=True).click()

        ## applying filtering inside askslot
        self.page.locator('//*[@class="add-filter-icon"]//img').nth(1).click()
        self.page.get_by_role("combobox").nth(3).fill('ph_number')
        self.page.get_by_role("combobox").nth(3).press("Enter")
        self.page.locator('//*[@role="combobox" and @id="Condition"]').click()
        self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Empty']''').click()

        self.page.locator("//button[normalize-space()='Done']").click()

        ## adding first questions inside ask slot
        self.page.locator('//*[@class="editable-field question-field"]').fill(
            '''<b>Please provide your phone number which you have used while booking your slot.</b>''')

        self.page.get_by_role("combobox").nth(2).click()

        ## adding validation atype ans save answer to slot value in Ask slot
        self.page.locator("//*[contains(@id,'listbox')]//descendant::div[text()='Phone No.']").click()
        self.page.get_by_role("combobox").nth(3).fill('ph_number')
        self.page.get_by_role("combobox").nth(3).press("Enter")
        self.page.get_by_role("button", name="Add Cards").click()

        ## add text card 3 card  with filters with service id empty true
        self.page.get_by_role("button", name="Add Cards").click()
        self.page.get_by_text("Text", exact=True).click()

        ## applying filtering inside text card by selecting service id

        self.page.locator("(//img[@title='Add Filter'])[3]").click()

        self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]").click()

        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "serviceId")

        self.page.keyboard.press("Enter")

        self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]").click()

        self.page.locator("(//div[contains(@class,'select__input-container css-4j0fso')])[1]").click()

        self.page.locator("//div[normalize-space(text()) ='Empty']").click()

        self.page.locator("(//button[normalize-space()='Done'])[1]").click()
        # self.page.locator('//*[@class="add-filter-icon"]//img').nth(2).click()
        # self.page.get_by_role("combobox").nth(7).click()
        #
        # ##service id can only be selected using this xpath
        # self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill("name")
        # # self.page.locator('//div[@class="select__option css-1nhws6w-option"]//following::div[@title="serviceId"]').click()
        # self.page.locator('//*[@role="combobox" and @id="Condition"]').click()
        # self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Empty']''').click()
        # self.page.locator("//button[normalize-space()='Done']").click()

        # inputing answer in 3 text card on node6
        self.page.locator("//div[@class='ql-editor ql-blank']").fill('''Sorry, I can't find any callback request.''')
        self.page.get_by_role("button", name="Add   Cards").click()

        ## adding a webhook card

        self.page.get_by_role("button", name="Add Cards").click()
        self.page.get_by_text("Webhook", exact=True).click()

        ## setting title in webhook card
        self.page.locator("//*[contains(@id,'wekbook-dropdown')]").click()
        self.page.locator(
            "//div[@class='select__option css-1nhws6w-option' and text()='ECB schedule callback - Cancel']").click()

        ##setting timezonein webhook card
        self.page.locator("//div[contains(text(),'asia/kolkata')]").clear()
        self.page.locator("//div[@class='editable-field']").nth(3).fill("{{$sys:TimeZoneName}}")

        ##setting service id in webhook card
        self.page.locator("//div[contains(text(),'1384-e32a1ba4-1287-4698-b82e-3caa902eb131')]").clear()
        self.page.locator("//div[@class='editable-field']").nth(6).fill("{{$local:serviceId}}")

        ##setting servicename in webhook card
        self.page.locator("//div[contains(text(),'request-tbs-wls-cb-pcs-sch-cr1-en')]").clear()
        self.page.locator("//div[@class='editable-field']").nth(7).fill("{{$local:serviceName}}")

        self.page.get_by_role("button", name="Add Cards").click()

        ## adding response textcard with response=200
        self.page.get_by_role("button", name="Add Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        ## applying filtering inside text card
        self.page.locator('//*[@class="add-filter-icon"]//img').nth(4).click()
        ##apply response=200 in filters inside text card
        self.page.locator("//input[@placeholder='Select Scope']").click()
        self.page.locator("//a[@id='ddwebhook']").click()

        # selecting slot
        self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]").click()

        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "sR.responseCode")

        self.page.keyboard.press("Enter")

        self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]").click()
        # self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]").click()
        # self.page.locator("//*[contains(@id,'listbox')]//descendant::div[@title='sR.responseCode']").click()
        self.page.locator('//*[@role="combobox" and @id="Condition"]').click()
        self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Equals']''').click()
        self.page.locator("//input[@placeholder='Value']").fill("200")

        self.page.locator("//button[normalize-space()='Done']").click()
        self.page.wait_for_timeout(500)

        self.page.locator("(//div[contains(@class,'ql-editor ql-blank')])").fill("Your callback has been cancelled.")

        self.page.get_by_role("button", name="Add Cards").click()

        ## adding last  textcard with response!=200
        self.page.get_by_role("button", name="Add Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        ## applying filtering inside text card
        self.page.locator('//*[@class="add-filter-icon"]//img').nth(5).click()
        ##apply response=200 in filters inside text card

        self.page.locator("//input[@placeholder='Select Scope']").click()
        self.page.locator("//a[@id='ddwebhook']").click()

        # selecting slot
        self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]").click()

        self.page.locator("//div[normalize-space(text()) ='Select']//following::input[@type='text'][1]").fill(
            "sR.responseCode")

        self.page.keyboard.press("Enter")

        self.page.locator("(//div[contains(@class,'select__input-container css-1duuv5x')])[2]").click()
        # self.page.get_by_role("combobox").nth(8).click()
        # self.page.locator("//*[contains(@id,'listbox')]//descendant::div[@title='sR.responseCode']").click()
        self.page.locator('//*[@role="combobox" and @id="Condition"]').click()
        self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Not Equals']''').click()
        self.page.locator("//input[@placeholder='Value']").fill("200")

        self.page.locator("//button[normalize-space()='Done']").click()

        # inputing answer in  text card

        self.page.locator("//div[@id='quilans5']//div[@class='ql-editor ql-blank']").fill(
            '''Sorry, We are unable to cancel your callback. Please try after some time.''')
        self.page.get_by_role("button", name="Add   Cards").click()
        # saving node and click on back button
        self.page.wait_for_timeout(800)
        self.page.locator("(//span[normalize-space()='Save'])[1]").click()
        self.page.wait_for_timeout(800)
        self.page.locator("//button[@class='btn b-other']").click()
        self.page.wait_for_timeout(500)
        self.page.locator("//button[@class='btn b-other']").click()
