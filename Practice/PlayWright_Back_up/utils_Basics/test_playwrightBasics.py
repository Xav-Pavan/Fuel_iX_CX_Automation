#use this package to import autosuggestions
from playwright.sync_api import Page

def test_playwrightBasics(playwright):
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context()
    #context used stroe all cockies and caches in single file
    page = context.new_page()
    page.goto("https://mqa2.xavlab.xyz/")
    print("basics")

#shortcut
#chromium headless mode, 1 sgingle context
#page comes from fixture and Page comes from packages
def test_playwrightShortCut(page:Page):
    page.goto("https://mqa2.xavlab.xyz/")
    print("shrot cuts")

