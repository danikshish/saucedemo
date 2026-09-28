import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.parametrize('email, password', [('standard_user', 'secret_sauce')])
def test_successful_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://www.saucedemo.com/')
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()


    # products_title = chromium_page.locator('[data-test="title"]')
    # expect(products_title).to_be_visible()
    # expect(products_title).to_have_text('Products')