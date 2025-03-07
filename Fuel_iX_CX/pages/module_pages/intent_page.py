
from Fuel_iX_CX.locators.intent_locators import IntentPageLocators


class IntentPage:

    def __init__(self, page):
        self.page = page

    def add_text_card(self, text_msg):
        intentlocators.ADD_CARDS_LINK.click()
        intentlocators.TEXT_CARD_BUTTON_ICON.click()
        intentlocators.INPUT_TEXT_TEXT_CARD.fill(text_msg)
        intentlocators.ADD_CARDS_LINK.click()

    def node_creation(self, NodetemplateTitle, nodequestion, textcardmsg):
        ## initializing instance of centralrepository_locator class
        global intentlocators
        intentlocators = IntentPageLocators(self.page)

        intentlocators.NODE_TEMPLATE_TITLE.fill(NodetemplateTitle)
        intentlocators.NODE_QUESTION.fill(nodequestion)
        self.add_text_card(textcardmsg)

        # Wait for up to 2 sec
        self.page.wait_for_timeout(500)
        intentlocators.SAVE_BUTTON.wait_for(state="visible", timeout=2000)  # Wait for up to 2 sec
        intentlocators.SAVE_BUTTON.click()

        actual_newnode_sucessmsg = intentlocators.NODE_TEMPLATE_CREATION_SUCCESS_MSG.inner_text()
        Expected__newnode_sucessmsg = "Template Created Successfully."
        assert actual_newnode_sucessmsg == Expected__newnode_sucessmsg, "Assertionfailed"
        print(f"{NodetemplateTitle} is successfully created and validated")

    def creating_schedule_callback_scenerio_get_available_slots_node(self, NodetemplateTitle, nodequestion,
                                                                     textcardmsg):
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_schedule_new_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.locator("//div[@class='rst__rowNodeAdd add-node-uid'][1]").click()
        self.page.get_by_text("New Node").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_booking_success_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[2]").click()
        self.page.get_by_text("New Node").nth(1).click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_reschedule_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[3]").click()
        self.page.locator("(//div[@class='flowMenuItem'][normalize-space()='New Node'])[3]").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_issue_occured_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.get_by_test_id("add-btn-flow").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_callBack_booking_failed_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.get_by_test_id("add-btn-flow").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def creating_canceling_callBack_request_node(self, NodetemplateTitle, nodequestion, textcardmsg):
        self.page.get_by_test_id("add-btn-flow").click()
        self.node_creation(NodetemplateTitle, nodequestion, textcardmsg)
        self.page.wait_for_timeout(500)
        intentlocators.BACK_BUTTON.wait_for(state="visible", timeout=2000)
        intentlocators.BACK_BUTTON.click()

    def scb_editing_issue_occurred_node(self):
        ##opening issue accured node for editing

        intentlocators.SCB_ISSUE_OCCURED_NODE.click()
        intentlocators.SCB_EDIT_ICON.click()

        # modifying textbox in textcard
        textCardTextBox = intentlocators.SCB_TEXT_CARD_TEXTBOX
        textCardTextBox.scroll_into_view_if_needed()
        textCardTextBox.wait_for(state='visible')
        textCardTextBox.clear()

        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill("I am facing some issues, please try after some time.")

        # saving node and click on back button
        self.page.wait_for_timeout(800)

        intentlocators.SCB_SAVE_BUTTON.click()

        self.page.wait_for_timeout(800)

        intentlocators.SCB_BACK_BUTTON.click()
        self.page.wait_for_timeout(500)

        intentlocators.SCB_BACK_BUTTON.click()

    def scb_editing_callBack_booking_failed_node(self):
        ##opening callBack_booking_failed node for editing

        intentlocators.SCB_CALLBACK_BOOKING_FAILED_NODE.click()
        intentlocators.SCB_EDIT_ICON.click()

        ##modifying text card by clearing text inside textbox
        textCardTextBox = intentlocators.SCB_TEXT_CARD_TEXTBOX
        textCardTextBox.scroll_into_view_if_needed()
        textCardTextBox.wait_for(state='visible')
        textCardTextBox.clear()

        ##modifying text card by inputing values inside textbox
        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill(
            '''Hmm, looks like that time slot is no longer available or you have already booked a time.''')

        ## adding 2 text card in the flow
        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_TEXT_CARD_BUTTON_ICON.click()

        ## input value in textcard textbox
        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill(
            '''Add Card,If you have recently booked a time we will be reaching out within an hour after your scheduled time.''')

        self.page.wait_for_timeout(500)

        ## adding a goto card
        intentlocators.SCB_GOTO_BUTTON.click()

        #clicking on goto after  adding a goto card
        intentlocators.SCB_SELECT_GOTO_CONTAINER.click()

        ## selecting node1 in gotocard
        intentlocators.SCB_SCHEDULE_GET_AVAILABLE_SLOTS.click()

        ## saving node and clicking on back button to move to intent template page
        self.page.wait_for_timeout(800)
        intentlocators.SCB_SAVE_BUTTON.click()

        self.page.wait_for_timeout(800)
        intentlocators.SCB_BACK_BUTTON.click()

        self.page.wait_for_timeout(500)
        intentlocators.SCB_BACK_BUTTON.click()

    def scb_editing_canceling_callBack_request_node(self):
        ## opening canceling_callBack_request_node for editing

        intentlocators.CANCELING_CALLBACK_NODE.click()
        intentlocators.SCB_EDIT_ICON.click()

        # self.page.locator("//*[@title='Canceling_CallBack_Request']").click()
        #
        # self.page.locator("//*[@data-action-type='edit']//img[@class='chatbot-header-icon']").click()

        ##modifying text card by clearing text inside textbox
        textCardTextBox = intentlocators.SCB_TEXT_CARD_TEXTBOX
        textCardTextBox.scroll_into_view_if_needed()
        textCardTextBox.wait_for(state='visible')
        textCardTextBox.clear()

        ##modifying text card by inputing values inside textbox
        intentlocators.SCB_TEXT_BLANK_TEXTBOX.fill('''Please wait we are Canceling your call back .......''')

        # adding 2card as  ask card slot with filter condition  ph_number empty true

        # self.page.get_by_role("button", name="Add Cards").click()
        # self.page.get_by_text("Ask Slots", exact=True).click()

        intentlocators.SCB_ADD_CARDS_BUTTON.click()
        intentlocators.SCB_ASK_SLOTS_BUTTON.click()

        ## applying filtering inside askslot
        intentlocators.SCB_ADD_FILTER_ICON.nth(1).click()
        ##setting ph_number as slot name inside filter
        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN.nth(3).fill('ph_number')
        intentlocators.SCB_SLOT_NAME_SELECT_DDOWN.nth(3).press("Enter")
        ##setting EMPTY  as Condition inside filter
        intentlocators.SCB_CONDITION_DROPDOWN.click()
        intentlocators.SCB_CONDITION_SELECT_EMPTY_DROPDOWN.click()
        # self.page.locator('//*[@class="add-filter-icon"]//img').nth(1).click()
        # self.page.get_by_role("combobox").nth(3).fill('ph_number')
        # self.page.get_by_role("combobox").nth(3).press("Enter")
        # self.page.locator('//*[@role="combobox" and @id="Condition"]').click()
        # self.page.locator('''//*[contains(@id,'listbox')]//descendant::div[text()='Empty']''').click()
        ## setting value as TRUE and click on done button in filter

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
