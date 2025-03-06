from Fuel_iX_CX.utils.imports import *
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@pytest.fixture(scope="function")
def page_fixture(playwright: Playwright, request):
    """Fixture to launch a browser and provide a Playwright page instance."""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    logging.info("🚀 Launching the browser...")

    yield page  # Provide the page instance to tests

    # Stop tracing and save the trace file
    trace_path = "reports/trace.zip"
    context.tracing.stop(path=trace_path)
    logging.info(f"Trace saved at: {trace_path}")

    # Capture a final success screenshot (optional)
    screenshot_dir = "reports/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Sanitize test case name to remove special characters
    test_case_name = re.sub(r'[<>:"/\\|?*]', '_', request.node.name)

    screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}_final.png")

    page.screenshot(path=screenshot_path)
    allure.attach.file(screenshot_path, name=f"{request.node.name} - Final Screenshot",
                       attachment_type=allure.attachment_type.PNG)

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
                allure.attach(str(call.excinfo), name=f"{test_case_name} - Failure Trace",
                              attachment_type=allure.attachment_type.TEXT)

            except Exception as e:
                logging.error(f"⚠️ Failed to capture screenshot: {e}")


@pytest.fixture(params=[("pulkit.kansal@telusinternational.com", "xd", "Shivi@0889")])
def logintestdata(request):
    """Fixture to provide login test data."""
    return request.param
