from typing import Pattern

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.link = page.locator(f'[data-test="{identifier}-sidebar-link"]')

    def check_visible(self, title: str):
        expect(self.link).to_be_visible()
        expect(self.link).to_have_text(title)

    def navigate(self, expected_url: Pattern[str]):
        self.link.click()
        self.check_current_url(expected_url)