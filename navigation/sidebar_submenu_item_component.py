from navigation.sidebar_list_item_component import SidebarListItemComponent
from playwright.sync_api import Page


class SidebarSubmenuItemComponent(SidebarListItemComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page, identifier)

        self.link = page.locator(f'[data-test="dynamic-catalog-{identifier}-link"]')

