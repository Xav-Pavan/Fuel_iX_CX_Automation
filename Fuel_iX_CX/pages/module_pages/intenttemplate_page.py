
from Fuel_iX_CX.locators.intenttemplate_locator import IntentTemplatePageLocators


class IntentTemplatePage:


    def __init__(self, page):
        self.page = page



    def add_template_name_to_new_intent(self):
        ## initializing instance of centralrepository_locator class
        global flowrepolocators
        intenttemplatelocators=IntentTemplatePageLocators(self.page)


        intenttemplatelocators.PROMPT_INPUT_BOX.fill("BA_Schedule_call_back_Scenario")
        intenttemplatelocators.PROMPT_OK_BUTTON.click()
        intenttemplatelocators.NODE_CREATION_PLUS_ICON.click()