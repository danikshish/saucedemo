from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class ProductsListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.locator('[data-test="title"]')
        self.sort = page.locator('[data-test="product-sort-container"]')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Products')

        expect(self.sort).to_be_visible()
