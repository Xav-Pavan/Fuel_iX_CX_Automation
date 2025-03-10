import os
import re
import time
import logging
import allure
import pytest
from playwright.sync_api import sync_playwright, Playwright

from Fuel_iX_CX.data.test_SCB_data import SCB_TestData

# Set up logging to track execution details and errors
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def initialize_page_fixture(playwright: Playwright):
    """Function to initialize Playwright browser, context, and page."""

    # Launch browser (headless=False to see execution, change to True for headless mode)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Create a new browser context

    page = context.new_page()  # Open a new page instance

    # Start tracing to capture screenshots, snapshots, and sources for debugging
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    logging.info("🚀 Launching the browser...")

    return browser, context, page  # Return initialized instances


@pytest.fixture(scope="function")
def page_fixture(playwright: Playwright, request):
    """
    Pytest fixture to provide a Playwright page instance.
    Ensures setup and teardown of browser for each test case.
    """

    # Initialize the browser, context, and page
    browser, context, page = initialize_page_fixture(playwright)

    yield page  # Yield the page instance for the test

    # Stop tracing and save the trace file
    # trace_path = "reports/trace.zip"
    # context.tracing.stop(path=trace_path)
    # logging.info(f"📝 Trace saved at: {trace_path}")

    # Capture a final screenshot before closing the browser
    screenshot_dir = os.path.join(SCB_TestData.SCREENSHOT_PATH)
    os.makedirs(screenshot_dir, exist_ok=True)  # Ensure the directory exists

    # Sanitize the test case name to remove special characters
    test_case_name = re.sub(r'[<>:"/\\|?*]', '_', request.node.name)

    # Generate a timestamp for uniqueness
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, f"{test_case_name}_final_{timestamp}.png")

    try:
        # Capture screenshot only if the page is still open
        if not page.is_closed():
            page.screenshot(path=screenshot_path)

            # Attach the final screenshot to the Allure report
            allure.attach.file(
                screenshot_path,
                name=f"{request.node.name} - Final Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        logging.error(f"⚠️ Failed to capture final screenshot: {e}")

    # Close the browser context and browser
    context.close()
    browser.close()
    logging.info("👋 Browser closed successfully.")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture a screenshot if a test case fails.
    The failure screenshot is attached to the Allure report.
    """

    outcome = yield  # Execute the test case and get the result
    report = outcome.get_result()  # Get the test report

    # If the test has failed, capture a screenshot
    if report.failed:
        page = item.funcargs.get("page_fixture")  # Retrieve the page fixture instance

        if page:
            try:
                # Check if the page is still open before capturing a screenshot
                if page.is_closed():
                    logging.error("❌ Page is already closed. Cannot capture a screenshot.")
                    return

                # Generate timestamp for unique screenshot naming
                timestamp = time.strftime("%Y%m%d_%H%M%S")

                # Define directory for failed test screenshots
                screenshot_dir = "reports/failed_screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)  # Ensure the directory exists

                # Sanitize test case name to remove special characters
                test_case_name = re.sub(r'[<>:"/\\|?*]', '_', item.name)

                # Define screenshot path for failed test case
                screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}_failed_{timestamp}.png")

                # Capture screenshot on failure
                page.screenshot(path=screenshot_path)
                logging.error(f"❌ Test '{test_case_name}' failed! Screenshot saved at: {screenshot_path}")

                # Attach the screenshot to the Allure report
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(image_file.read(), name=f"{test_case_name} - Failure Screenshot",
                                  attachment_type=allure.attachment_type.PNG)

                # Attach failure message to Allure report
                error_message = str(call.excinfo)
                allure.attach(
                    error_message,
                    name=f"{test_case_name} - Failure Trace",
                    attachment_type=allure.attachment_type.TEXT
                )

                # Log failure details
                logging.error(f"🔴 Test Case Failed: {test_case_name}")
                logging.error(f"🔴 Error Message: {error_message}")

            except Exception as e:
                logging.error(f"⚠️ Failed to capture failure screenshot: {e}")
