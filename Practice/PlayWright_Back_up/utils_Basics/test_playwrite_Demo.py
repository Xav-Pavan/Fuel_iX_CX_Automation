import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mqa2.xavlab.xyz/")
    page.get_by_placeholder("Enter email").click()
    page.get_by_placeholder("Enter email").fill("puchha.pavan@telusinternational.com")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Enter domain").click()
    page.get_by_placeholder("Enter domain").fill("xd")
    page.get_by_placeholder("Enter domain").press("Enter")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Enter password").click()
    page.get_by_placeholder("Enter password").fill("*Pavan@4331")
    page.get_by_role("button", name="Login").click()
    page.locator("li:nth-child(4) > a").click()
    page.get_by_role("link", name="FLOW", exact=True).click()
    page.locator("div:nth-child(50) > .rst__node > .rst__nodeContent > div > div > .rst__expandButton").click()
    page.get_by_text("Rename").click()
    page.get_by_test_id("promptinputbox").fill("one")
    page.get_by_test_id("promptokbutton").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
