import json
import os

def get_test_data():
    """Fetch test data from test_data.json using a dynamic project root path."""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)# Get the directory of the current script
    PROJECT_ROOT = os.path.dirname(BASE_DIR)  # Move up to project_root
    relative_path = os.path.join(PROJECT_ROOT, "data", "test_data.json")  # Dynamic path

    if not os.path.exists(relative_path):  # Check if file exists
        raise FileNotFoundError(f"Error: File not found - {relative_path}")

    with open(relative_path, "r", encoding="utf-8") as file:
        return json.load(file)  # Load JSON data

# Example usage
try:
    test_data = get_test_data()
    print("Test data loaded successfully:", test_data)
except Exception as e:
    print(e)
