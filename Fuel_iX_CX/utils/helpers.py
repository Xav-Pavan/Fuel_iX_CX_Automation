import json


def get_test_data():
    with open("C:/Users/puchha.pavan/PycharmProjects/PyTest_Python/Fuel_iX_CX/data/test_data.json") as file:
        return json.load(file)
