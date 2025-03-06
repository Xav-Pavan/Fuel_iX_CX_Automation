import json


def get_test_data():
    with open("C:/Users/pulkit.kansal/v.1/PyTest_Python/Fuel_iX_CX/data/login_test.json") as file:
        return json.load(file)



def get_scb_test_data():
    with open("C:/Users/pulkit.kansal/v.1/PyTest_Python/Fuel_iX_CX/data/scb_test.json") as file:
        return json.load(file)