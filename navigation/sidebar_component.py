import re

from components.base_component import BaseComponent
from playwright.sync_api import Page

from navigation.navbar_component import NavbarComponent
from navigation.sidebar_list_item_component import SidebarListItemComponent
from navigation.sidebar_submenu_item_component import SidebarSubmenuItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.all_items = SidebarListItemComponent(page, 'inventory')
        self.dynamic_catalog = SidebarListItemComponent(page, 'dynamic-catalog')
        self.lazy_load_dynamic_catalog_item = SidebarSubmenuItemComponent(page, 'lazy-load')
        self.spinner_dynamic_catalog_item = SidebarSubmenuItemComponent(page, 'spinner')
        self.slider_dynamic_catalog_item = SidebarSubmenuItemComponent(page, 'slider')
        self.about = SidebarListItemComponent(page, 'about')
        self.logout = SidebarListItemComponent(page, 'logout')
        self.reset_app_state = SidebarListItemComponent(page, 'reset')

    def check_visible(self):
        self.all_items.check_visible('All Items')

        self.dynamic_catalog.check_visible('Dynamic Catalog')
        self.dynamic_catalog.link.click()

        self.lazy_load_dynamic_catalog_item.check_visible('Lazy Load')
        self.spinner_dynamic_catalog_item.check_visible('Spinner')
        self.slider_dynamic_catalog_item.check_visible('Slider')

        self.about.check_visible('About')
        self.logout.check_visible('Logout')
        self.reset_app_state.check_visible('Reset App State')


    def click_all_items(self):
        self.navbar.menu_button.click()
        self.all_items.navigate(re.compile(r".*/inventory.html"))

    def click_lazy_load(self):
        self.navbar.menu_button.click()
        self.dynamic_catalog.link.click()
        self.lazy_load_dynamic_catalog_item.navigate(re.compile(r".*/dynamic-catalog-lazy-load.html"))

    def click_spinner(self):
        self.navbar.menu_button.click()
        self.dynamic_catalog.link.click()
        self.spinner_dynamic_catalog_item.navigate(re.compile(r".*/dynamic-catalog-spinner.html"))

    def click_slider(self):
        self.navbar.menu_button.click()
        self.dynamic_catalog.link.click()
        self.slider_dynamic_catalog_item.navigate(re.compile(r".*/dynamic-catalog-slider.html"))

    def click_logout(self):
        self.navbar.menu_button.click()
        self.logout.navigate(re.compile(r".*saucedemo\.com/?$"))

