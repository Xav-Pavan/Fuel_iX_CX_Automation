import json
import os


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
    print(e)
