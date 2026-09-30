from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class ProductViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.locator('[data-test="inventory-item-name"]')
        self.description = page.locator('[data-test="inventory-item-desc"]')
        self.price = page.locator('[data-test="inventory-item-price"]')

    def check_visible(self, title: str, description: str, price: str, identifier: str, index: int):
        image = self.page.locator(f'[data-test="inventory-item-sauce-labs-{identifier}-img"]')
        add_to_card_button = self.page.locator(f'[data-test="add-to-cart-sauce-labs-{identifier}"]')

        expect(image).to_be_visible()
        expect(add_to_card_button).to_be_visible()

        expect(add_to_card_button).to_be_visible()
        expect(add_to_card_button).to_have_text('Add to cart')

        expect(self.title.nth(index)).to_be_visible()
        expect(self.title.nth(index)).to_have_text(title)

        expect(self.description.nth(index)).to_be_visible()
        expect(self.description.nth(index)).to_have_text(description)

        expect(self.price.nth(index)).to_be_visible()
        expect(self.price.nth(index)).to_have_text(f'${price}')

    def click_add_to_card_button(self, identifier: str):
        add_to_card_button = self.page.locator(f'[data-test="add-to-cart-sauce-labs-{identifier}"]')
        remove_button = self.page.locator(f'[data-test="remove-sauce-labs-{identifier}"]')

        add_to_card_button.click()
        expect(remove_button).to_be_visible()

    def click_remove_button(self, identifier: str):
        add_to_card_button = self.page.locator(f'[data-test="add-to-cart-sauce-labs-{identifier}"]')
        remove_button = self.page.locator(f'[data-test="remove-sauce-labs-{identifier}"]')

        expect(remove_button).to_be_visible()
        remove_button.click()
        expect(add_to_card_button).to_be_visible()