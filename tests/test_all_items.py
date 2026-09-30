import pytest
from pages.all_items_page import AllItemsPage

@pytest.mark.all_items
@pytest.mark.regression
def test_all_items_displaying(all_items_page: AllItemsPage):
    all_items_page.visit('https://www.saucedemo.com/inventory.html')
    all_items_page.navbar.check_visible()
    all_items_page.check_visible_products_title()
    all_items_page.check_visible_product(
        title='Sauce Labs Backpack',
        description='carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.',
        price='29.99',
        identifier='backpack',
        index=0
    )
    all_items_page.check_visible_product(
        title='Sauce Labs Bike Light',
        description="A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
        price='9.99',
        identifier='bike-light',
        index=1
    )
    all_items_page.check_visible_product(
        title='Sauce Labs Bolt T-Shirt',
        description='Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.',
        price='15.99',
        identifier='bolt-t-shirt',
        index=2
    )
    all_items_page.check_visible_product(
        title='Sauce Labs Fleece Jacket',
        description="It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
        price='49.99',
        identifier='fleece-jacket',
        index=3
    )
    all_items_page.check_visible_product(
        title='Sauce Labs Onesie',
        description="Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
        price='7.99',
        identifier='onesie',
        index=4
    )

@pytest.mark.all_items
@pytest.mark.regression
def test_add_to_cart(all_items_page: AllItemsPage):
    all_items_page.visit('https://www.saucedemo.com/inventory.html')
    all_items_page.click_add_to_card_button('backpack')
    all_items_page.navbar.check_visible_cart_count('1')

    all_items_page.click_add_to_card_button('bike-light')
    all_items_page.navbar.check_visible_cart_count('2')

    all_items_page.click_add_to_card_button('bolt-t-shirt')
    all_items_page.navbar.check_visible_cart_count('3')

    all_items_page.click_add_to_card_button('fleece-jacket')
    all_items_page.navbar.check_visible_cart_count('4')

    all_items_page.click_add_to_card_button('onesie')
    all_items_page.navbar.check_visible_cart_count('5')

    all_items_page.click_remove_button('onesie')
    all_items_page.navbar.check_visible_cart_count('4')

    all_items_page.click_remove_button('fleece-jacket')
    all_items_page.navbar.check_visible_cart_count('3')

    all_items_page.click_remove_button('bolt-t-shirt')
    all_items_page.navbar.check_visible_cart_count('2')

    all_items_page.click_remove_button('bike-light')
    all_items_page.navbar.check_visible_cart_count('1')

    all_items_page.click_remove_button('backpack')
    all_items_page.navbar.check_no_cart_count()

@pytest.mark.sidebar
@pytest.mark.regression
def test_sidebar_visible(all_items_page: AllItemsPage):
    all_items_page.visit('https://www.saucedemo.com/inventory.html')
    all_items_page.navbar.click_menu_button()
    all_items_page.sidebar_component.check_visible()


@pytest.mark.sidebar
@pytest.mark.regression
def test_sidebar_navigation(all_items_page: AllItemsPage):
    all_items_page.visit('https://www.saucedemo.com/inventory.html')
    all_items_page.sidebar_component.click_lazy_load()
    all_items_page.sidebar_component.click_spinner()
    all_items_page.sidebar_component.click_slider()
    all_items_page.sidebar_component.click_all_items()
    all_items_page.sidebar_component.click_logout()










