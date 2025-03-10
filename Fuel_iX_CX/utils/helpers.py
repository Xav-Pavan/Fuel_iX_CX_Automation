import json
import os
import time
import allure
from Fuel_iX_CX.data.test_SCB_data import SCB_TestData


def get_test_data(file_name="test_data.json"):
    """Fetch test data from the specified JSON file using a dynamic project root path."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(project_root, "data", file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: File not found - {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_scb_test_data():
    """Fetch SCB test data dynamically using get_test_data()."""
    return get_test_data("scb_test.json")


# Example usage
try:
    test_data = get_test_data()  # Fetch test_data.json
    print("Test data loaded successfully:", test_data)

    scb_test_data = get_scb_test_data()  # Fetch scb_test.json
    print("SCB test data loaded successfully:", scb_test_data)
except Exception as e:
    print(f"⚠️ Error loading test data: {e}")


def save_screenshot(page, screenshot_filename):
    """
    Captures and saves a screenshot at the defined path and attaches it to Allure reports.

    :param page: Playwright page instance
    :param screenshot_filename: Name of the screenshot file (without extension)
    """
    # Ensure the screenshot directory exists
    os.makedirs(SCB_TestData.SCREENSHOT_PATH, exist_ok=True)

    # Generate timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    # Construct the full screenshot path
    screenshot_path = os.path.join(SCB_TestData.SCREENSHOT_PATH, f"{screenshot_filename}_{timestamp}{SCB_TestData.FILE_TYPE}")

    # Capture and save the screenshot
    page.screenshot(path=screenshot_path)

    # Attach screenshot to Allure report
    allure.attach.file(
        screenshot_path,
        name=f"{screenshot_filename}_{timestamp}",
        attachment_type=allure.attachment_type.PNG
    )

    # Logging (optional)
    print(f"✅ Screenshot saved at: {screenshot_path}")

    return screenshot_path  # Return the path for further reference if needed
