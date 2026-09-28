import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.saucedemo.com/')

    email_input = page.locator('[data-test="username"]')
    email_input.fill('standard_user')

    password_input = page.locator('[data-test="password"]')
    password_input.fill('secret_sauce')

    login_button = page.locator('[data-test="login-button"]')
    login_button.click()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    browser.close()