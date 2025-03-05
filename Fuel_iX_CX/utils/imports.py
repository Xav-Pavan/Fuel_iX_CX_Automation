# imports.py - Centralized Import File

import pytest
import allure

# Importing page classes
from Fuel_iX_CX.pages.Schedule_CallBack_Dashboard import Schedule_Call_Back_Dashboard
from Fuel_iX_CX.pages.Schedule_CallBack_Intent_Import import Import_SCB_Intent
from Fuel_iX_CX.pages.Schedule_CallBack_Widget import Schedule_Call_Back_Widget
from Fuel_iX_CX.pages.login_page import LoginPage
from Fuel_iX_CX.pages.Schedule_Call_Back_Nodes_Handler import Schedule_Call_Back_Nodes
from Fuel_iX_CX.pages.Schedule_CallBack_Page_Handler import Schedule_Call_Back
from Fuel_iX_CX.objects.page_objects import initialize_page_objects
from _pytest import logging

import json
import pytest
import os
from Fuel_iX_CX.data.test_SCB_data import *
import re  # Added to sanitize filenames
from playwright.sync_api import Playwright
import allure  # Import Allure for reporting

from Fuel_iX_CX.locators.login_locators import LoginPageLocators

from Fuel_iX_CX.utils.config import BASE_URL

# Utility imports
from Fuel_iX_CX.utils.helpers import get_test_data
