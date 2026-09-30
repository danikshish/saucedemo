from typing import Pattern

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = page.locator('[class="app_logo"]')
        self.menu_button = page.locator('[id="react-burger-menu-btn"]')
        self.shopping_cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.shopping_cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def check_visible(self):
        expect(self.app_title).to_be_visible()
        expect(self.app_title).to_have_text('Swag Labs')

        expect(self.menu_button).to_be_visible()

        expect(self.shopping_cart_link).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.shopping_cart_link.click()
        self.check_current_url(expected_url)

    def click_menu_button(self):
        self.menu_button.click()

    def check_visible_cart_count(self, expected_count: str):
        expect(self.shopping_cart_badge).to_be_visible()
        expect(self.shopping_cart_badge).to_have_text(expected_count)

    def check_no_cart_count(self):
        expect(self.shopping_cart_badge).to_be_hidden()