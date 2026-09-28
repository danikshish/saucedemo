import pytest
from playwright.sync_api import Page

from pages.all_item_page import AllItemPage
from pages.login_page import LoginPage

@pytest.fixture
def login_page(chromium_page_with_state: Page) -> LoginPage:
    return LoginPage(page=chromium_page_with_state)

def all_item_page(chromium_page_with_state: Page) -> AllItemPage:
    return AllItemPage(page=chromium_page_with_state)