def test_screenshot_on_failure(browser_context):
    page = browser_context
    page.goto("https://google.com")
    page.locator("//button[text()='Submit']").click()  # If the button doesn't exist, it fails
