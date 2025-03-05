import pytest
from playwright.sync_api import sync_playwright, Playwright


@pytest.fixture(scope='session')
def user_cred(request):
    return request.param


@pytest.fixture(scope="function")
def browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    # Stop tracing and save the trace file
    context.tracing.stop(path=f"trace.zip")
    browser.close()
