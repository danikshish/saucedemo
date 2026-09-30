from navigation.navbar_component import NavbarComponent
from navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class AllItemsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar_component = SidebarComponent(page)

        self.products_title = page.locator('[data-test="title"]')
        self.product_title = page.locator('[data-test="inventory-item-name"]')
        self.product_description = page.locator('[data-test="inventory-item-desc"]')
        self.product_price = page.locator('[data-test="inventory-item-price"]')


    def check_visible_products_title(self):
        expect(self.products_title).to_be_visible()
        expect(self.products_title).to_have_text('Products')

    def check_visible_product(self, title: str, description: str, price: str, identifier: str, index: int):
        product_image = self.page.locator(f'[data-test="inventory-item-sauce-labs-{identifier}-img"]')

        expect(product_image).to_be_visible()

        expect(self.product_title.nth(index)).to_be_visible()
        expect(self.product_title.nth(index)).to_have_text(title)

        expect(self.product_description.nth(index)).to_be_visible()
        expect(self.product_description.nth(index)).to_have_text(description)

        expect(self.product_price.nth(index)).to_be_visible()
        expect(self.product_price.nth(index)).to_have_text(f'${price}')

    def click_add_to_card_button(self, identifier: str):
        product_add_to_card_button = self.page.locator(f'[data-test="add-to-cart-sauce-labs-{identifier}"]')
        product_remove_button = self.page.locator(f'[data-test="remove-sauce-labs-{identifier}"]')

        expect(product_add_to_card_button).to_be_visible()
        product_add_to_card_button.click()
        expect(product_remove_button).to_be_visible()

    def click_remove_button(self, identifier: str):
        product_add_to_card_button = self.page.locator(f'[data-test="add-to-cart-sauce-labs-{identifier}"]')
        product_remove_button = self.page.locator(f'[data-test="remove-sauce-labs-{identifier}"]')

        expect(product_remove_button).to_be_visible()
        product_remove_button.click()
        expect(product_add_to_card_button).to_be_visible()

