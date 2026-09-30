import pytest
from playwright.sync_api import Page

from pages.all_items_page import AllItemsPage
from pages.login_page import LoginPage

@pytest.fixture
def login_page(chromium_page_with_state: Page) -> LoginPage:
    return LoginPage(page=chromium_page_with_state)

@pytest.fixture
def all_items_page(chromium_page_with_state: Page) -> AllItemsPage:
    return AllItemsPage(page=chromium_page_with_state)