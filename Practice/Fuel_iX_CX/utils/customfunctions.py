class CustomFunctions:


    def __init__(self,page):
        self.page=page


    def add_text_card(self,text_msg):
        self.page.get_by_role("button", name="Add Cards").click()
        self.page.get_by_text("Text", exact=True).click()
        self.page.get_by_role("paragraph").fill(text_msg)
        self.page.get_by_role("button", name="Add Cards").click()

    def node_creation(self,NodetemplateTitle, nodequestion, textcardmsg):
        self.page.get_by_placeholder("Enter template title here").fill(NodetemplateTitle)  # enter title to node
        self.page.locator(".questions-rich-text-area").fill(nodequestion)  # enter question

        self.AddtextCard(textcardmsg)

        self.page.get_by_role("button", name="Save").click()

        actual_newnode_sucessmsg = self.page.locator("//*[@class='MuiAlert-message css-1xsto0d']").inner_text()
        Expected__newnode_sucessmsg = "Template Created Successfully."
        assert actual_newnode_sucessmsg == Expected__newnode_sucessmsg, "Assertionfailed"
        print(f"{NodetemplateTitle} is successfully created and validated")

