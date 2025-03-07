import json


def get_test_data():
    with open("C:/Users/anshu.sharma/Fuel_iX_CX_Automation/Fuel_iX_CX/data/test_data.json") as file:
        return json.load(file)
