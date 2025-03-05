import time

import pytest
from playwright.sync_api import Playwright, expect,Page
@pytest.fixture(scope="function")
def setup(playwright:Playwright):
     global page
     browser = playwright.chromium.launch(headless=False)
     context = browser.new_context()
     page = context.new_page()
     context.tracing.start(screenshots=True, snapshots=True, sources=True)

     yield
     context.tracing.stop(path="trace.zip")
     context.close()
     browser.close()

def Login_to_virtual_assistant_application(setup,logintestdata):

        page.goto("https://mqa2.xavlab.xyz/")
        page.get_by_placeholder("Enter email").fill(logintestdata[0])
        page.get_by_role("button", name="Login").click()
        page.get_by_placeholder("Enter domain").fill(logintestdata[1])
        page.get_by_role("button", name="Login").click()
        page.get_by_placeholder("Enter password").fill(logintestdata[2])
        page.get_by_role("button", name="Login").click()
        expect(page.locator("//span[@title='Analytics & Reports']")).to_contain_text("Analytics")
        print("login to Vertical assistant Webapplication is successfully Completed")


def AddtextCard(text_msg):

    page.get_by_role("button", name="Add Cards").click()
    page.get_by_text("Text", exact=True).click()
    page.get_by_role("paragraph").fill(text_msg)
    page.get_by_role("button", name="Add Cards").click()

def nodecreation(NodetemplateTitle,nodequestion,textcardmsg):
    page.get_by_placeholder("Enter template title here").fill(NodetemplateTitle)  # enter title to node
    page.locator(".questions-rich-text-area").fill(nodequestion)  # enter question

    AddtextCard(textcardmsg)
    time.sleep(5)
    page.get_by_role("button", name="Save").click()

    actual_newnode_sucessmsg = page.locator("//*[@class='MuiAlert-message css-1xsto0d']").inner_text()
    Expected__newnode_sucessmsg = "Template Created Successfully."
    assert actual_newnode_sucessmsg == Expected__newnode_sucessmsg, "Assertionfailed"
    print(f"{NodetemplateTitle} is successfully created and validated")






def test_NewFolderCreationInFlowRepository(setup, logintestdata):
    Login_to_virtual_assistant_application(setup, logintestdata)

    #click on cr
    page.locator("//li[@data-tip='Central Repository']//a").click()
    print("Cenrtal Repository Icon is succesfully clicked")
    # click on Flow cr
    page.get_by_role("link", name="FLOW", exact=True).click()
    print(" Flow type Central Repository Icon is successfully clicked")
    # create new folder in cr
    page.get_by_text("Add New Folder").click()
    page.get_by_test_id("promptinputbox").fill("playwrightAutomationTestFolder")
    page.get_by_test_id("promptokbutton").click()
    actual_newFolder_sucessmsg = page.locator("//*[@class='MuiAlert-message css-1xsto0d']").inner_text()
    Expected__newFolder_sucessmsg = "Added successfully!"
    assert actual_newFolder_sucessmsg == Expected__newFolder_sucessmsg, "Assertionfailed"
    print("New Folder is successfully created and validated")

    #creating new intent in folder
    page.get_by_test_id("btn-click").click()
    page.get_by_test_id("styl-btn").get_by_text("New Intent").click()
    page.get_by_test_id("promptinputbox").fill('Pulkit_Customer_FallBack_Intent')
    page.get_by_test_id("promptokbutton").click()

    ## Creating first node of schedule callback scenerio
    page.get_by_test_id("add-btn-flow").click()  # click on +icon to add first node

    nodecreation('Automated Schedule_CallBack-Node1', 'run scb scenerio','Automated Schedule_CallBack-Node1 is triggered sucessfully')
    page.get_by_test_id("backbutton-btn").click()


    ## creating second node

    page.locator("//div[@class='rst__rowNodeAdd add-node-uid'][1]").click()

    page.get_by_text("New Node").click()

    nodecreation('Schedule_New_CallBack_Request', 'create new call back request',
                 'Automated Schedule_CallBack-Node2 is triggered sucessfully')
    page.get_by_test_id("backbutton-btn").click()


    # creating 3rd node

    page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[2]").click()

    page.get_by_text("New Node").nth(1).click()

    nodecreation('booking success', 'create booking success',
                 ' booking success triggered sucessfully')
    page.get_by_test_id("backbutton-btn").click()

    # creating 4TH node

    page.locator("(//div[@class='rst__rowNodeAdd add-node-uid'])[3]").click()

    page.locator("(//div[@class='flowMenuItem'][normalize-space()='New Node'])[3]").click()

    nodecreation('reschedule', 'create reschedule node',
                 'reschedule node  triggered sucessfully')
    page.get_by_test_id("backbutton-btn").click()



    # 5th node
    page.get_by_test_id("add-btn-flow").click()

    nodecreation('issue occured', 'create issue occured node',
                 'issue is accured Phone number is invalid one')
    page.get_by_test_id("backbutton-btn").click()



    # 6 node

    page.get_by_test_id("add-btn-flow").click()
    nodecreation('booking faild', 'create booking faild node',
                 'booking faild is triggered')
    page.get_by_test_id("backbutton-btn").click()


   # 7th node
    page.get_by_test_id("add-btn-flow").click()

    nodecreation('booking cancel request', 'create booking canceling node',
                 'booking canceling node is triggered')
    page.get_by_test_id("backbutton-btn").click()



    page.pause()




