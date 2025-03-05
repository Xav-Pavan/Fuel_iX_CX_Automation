import pytest
from playwright.sync_api import expect, Playwright


@pytest.fixture(scope="function")
def setup(playwright: Playwright,logintestdata):
    global page
    global ThumbsDown_BeforeFeedback
    browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context(record_video_dir="../videos/",
    #record_video_size={"width": 800, "height": 800})
    context = browser.new_context()
    page = context.new_page()

  #  context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Make sure to close, so that videos are saved.

    yield
   # context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


def test_ThumbsDown_Check(setup,logintestdata):
    page.goto("https://mqa2.xavlab.xyz/")
    page.get_by_placeholder("Enter email").fill(logintestdata[0])
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Enter domain").fill(logintestdata[1])
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Enter password").fill(logintestdata[2])
    page.get_by_role("button", name="Login").click()
    expect(page.locator("//span[@title='Analytics & Reports']")).to_contain_text("Analytics")
 #   page.screenshot(path="../screenshot/scrrenshot3.png")

    ThumbsDown_BeforeFeedback = page.locator("//div[contains(@class,'report accuracy')]//div[contains(@class,'mt-lg-4')]//descendant::p[2]").inner_text()
    print(ThumbsDown_BeforeFeedback)

    page.locator("//button[@aria-label='Open Chat']").is_hidden()
    page.locator("//button[@aria-label='Open Chat']").is_visible()
    page.locator("//button[@aria-label='Open Chat']").click()
    page.get_by_text("Transaction Bot MQA").click()

    page.locator("//*[@id='user-input-message']").fill("explain what is feedback, feedback note and sorce")
    page.locator("//*[@id='msgSenderButton']").click()
    expect(page.get_by_role('button', name='Thumbs Down')).to_be_visible()
    page.get_by_role('button', name='Thumbs Down').click()
    msg = page.locator("//*[@class='custom-feedback']//button").inner_text()
    print(msg)
    page.locator("//*[@class='custom-feedback']//button").click()
    page.get_by_role("button", name="Irrelevant").click()
    page.get_by_test_id("input-msg-feedback-textbox").fill("ThumbsDown-feedback using playwright-tool")
    page.get_by_test_id("submit-msg-feedback-button").click()
    page.pause()
    page.locator("//span[contains(@title,'Refresh Dashboard')]//img[contains(@class,'chatbot-header-icon')]").click()
    ThumbsDowncountAfterFeedback = page.locator("//div[contains(@class,'report accuracy')]//div[contains(@class,'mt-lg-4')]//descendant::p[2]").inner_text()
    assert int(ThumbsDowncountAfterFeedback) == int(ThumbsDown_BeforeFeedback) + 1











