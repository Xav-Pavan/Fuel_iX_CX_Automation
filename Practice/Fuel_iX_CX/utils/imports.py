# imports.py - Centralized Import File

import pytest
import allure

# Importing page classes
from Practice.Fuel_iX_CX.pages.Schedule_CallBack_Dashboard import Schedule_Call_Back_Dashboard
from Practice.Fuel_iX_CX.pages.Schedule_CallBack_Intent_Import import Import_SCB_Intent
from Practice.Fuel_iX_CX.pages.Schedule_CallBack_Widget import Schedule_Call_Back_Widget
from Practice.Fuel_iX_CX.pages.login_page import LoginPage
from Practice.Fuel_iX_CX.pages.analyticsanddashboard_page import DashBoardPage
from Practice.Fuel_iX_CX.pages.Schedule_Call_Back_Nodes_Handler import Schedule_Call_Back_Nodes
from Practice.Fuel_iX_CX.pages.Schedule_CallBack_Page_Handler import Schedule_Call_Back
from Practice.Fuel_iX_CX.objects.page_objects import initialize_page_objects
from _pytest import logging
import time
import json
import pytest
import os
import re  # Added to sanitize filenames
from playwright.sync_api import Playwright
import allure  # Import Allure for reporting


from Practice.Fuel_iX_CX.locators.login_locators import LoginPageLocators

from Practice.Fuel_iX_CX.utils.config import BASE_URL

# Utility imports
from Practice.Fuel_iX_CX.utils.helpers import get_test_data
