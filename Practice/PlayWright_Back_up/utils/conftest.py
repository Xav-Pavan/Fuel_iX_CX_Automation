# import logging
# 
# import pytest
# from playwright.sync_api import Playwright
# # Set up logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# 
# @pytest.fixture(scope='session')
# def user_cred(request):
#     return request.param
# 
# 
# @pytest.fixture(scope="function")
# def browser_context(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
# 
#     # Start tracing
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     logging.info("Launching browser...")
# 
#     yield context
# 
#     # Stop tracing and save the trace file
#     context.tracing.stop(path=f"trace.zip")
#     context.close()
#     logging.info("Closing browser...")
#     browser.close()

import logging
import pytest
import time
import os
from playwright.sync_api import Playwright

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@pytest.fixture(scope='session')
def user_cred(request):
    return request.param


@pytest.fixture(scope="function")
def browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    logging.info("Launching browser...")

    yield page  # Returning page instead of context for easier use in BA_UseCases

    # Stop tracing and save the trace file
    context.tracing.stop(path="trace.zip")
    context.close()
    logging.info("Closing browser...")
    browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure with timestamp"""
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("browser_context")  # Get the page fixture
        if page:
            # Generate timestamp in format YYYYMMDD_HHMMSS
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_dir = r"C:/Users/puchha.pavan/PycharmProjects/PyTest_Python/PlayWright/TestResults/screenshots"

            # Ensure the directory exists
            os.makedirs(screenshot_dir, exist_ok=True)

            # Construct screenshot path with timestamp
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")

            # Capture screenshot
            page.screenshot(path=screenshot_path)
            logging.error(f"Test failed! Screenshot saved at: {screenshot_path}")

