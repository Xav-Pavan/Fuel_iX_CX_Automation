from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Launch Chrome (Chromium) with UI
    page = browser.new_page()
    page.goto("https://www.youtube.com")  # Open YouTube
    print("Page Title:", page.title())  # Print the page title
    browser.close()  # Close the browser

