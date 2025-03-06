import os
import re
import time
import logging
import allure
import pytest
from playwright.sync_api import sync_playwright, Playwright

from Fuel_iX_CX.data.test_SCB_data import SCB_TestData

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def initialize_page_fixture(playwright: Playwright):
    """Function to initialize Playwright browser, context, and page."""
    browser = playwright.chromium.launch(headless=False)  # Change to True for headless mode
    context = browser.new_context()
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    logging.info("🚀 Launching the browser...")

    return browser, context, page


@pytest.fixture(scope="function")
def page_fixture(playwright: Playwright, request):
    """Fixture to provide a Playwright page instance using `initialize_page_fixture()`."""
    browser, context, page = initialize_page_fixture(playwright)

    yield page  # Provide the page instance to tests

    # Stop tracing and save the trace file
    # trace_path = "reports/trace.zip"
    # context.tracing.stop(path=trace_path)
    # logging.info(f"📝 Trace saved at: {trace_path}")

    # Capture a final success screenshot
    screenshot_dir = os.path.join(SCB_TestData.SCREENSHOT_PATH)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Sanitize test case name to remove special characters
    test_case_name = re.sub(r'[<>:"/\\|?*]', '_', request.node.name)

    # Generate timestamp for uniqueness
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, f"{test_case_name}_final_{timestamp}.png")

    try:
        if not page.is_closed():
            page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name=f"{request.node.name} - Final Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        logging.error(f"⚠️ Failed to capture final screenshot: {e}")

    context.close()
    browser.close()
    logging.info("👋 Browser closed successfully.")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot on test failure and attach it to Allure report globally."""
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page_fixture")  # Get page fixture instance
        if page:
            try:
                if page.is_closed():
                    logging.error("❌ Page is already closed. Cannot capture a screenshot.")
                    return

                # Generate timestamp for unique screenshot naming
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                screenshot_dir = "reports/failed_screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)

                # Sanitize test case name to remove special characters
                test_case_name = re.sub(r'[<>:"/\\|?*]', '_', item.name)

                screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}_failed_{timestamp}.png")

                # Capture screenshot
                page.screenshot(path=screenshot_path)
                logging.error(f"❌ Test '{test_case_name}' failed! Screenshot saved at: {screenshot_path}")

                # Attach the screenshot to the Allure report
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(image_file.read(), name=f"{test_case_name} - Failure Screenshot",
                                  attachment_type=allure.attachment_type.PNG)

                # Attach failure message to Allure
                error_message = str(call.excinfo)
                allure.attach(
                    error_message,
                    name=f"{test_case_name} - Failure Trace",
                    attachment_type=allure.attachment_type.TEXT
                )

                logging.error(f"🔴 Test Case Failed: {test_case_name}")
                logging.error(f"🔴 Error Message: {error_message}")

            except Exception as e:
                logging.error(f"⚠️ Failed to capture failure screenshot: {e}")


@pytest.fixture(params=[("pulkit.kansal@telusinternational.com", "xd", "Shivi@0889")])
def logintestdata(request):
    """Fixture to provide login test data."""
    return request.param
