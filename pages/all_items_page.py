from components.products.product_view_component import ProductViewComponent
from components.products.products_list_toolbar_view_component import ProductsListToolbarViewComponent
from navigation.navbar_component import NavbarComponent
from navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class AllItemsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar_component = SidebarComponent(page)
        self.product_view = ProductViewComponent(page)
        self.toolbar_view = ProductsListToolbarViewComponent(page)





