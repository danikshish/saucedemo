import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.parametrize(
    'email, password', [('email', 'password'), ('email', 'okok')]
)
def test_unsuccessful_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://www.saucedemo.com/')
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()



    # chromium_page.goto('https://www.saucedemo.com/')
    #
    # email_input = chromium_page.locator('[data-test="username"]')
    # email_input.fill(email)
    #
    # password_input = chromium_page.locator('[data-test="password"]')
    # password_input.fill(password)
    #
    # login_button = chromium_page.locator('[data-test="login-button"]')
    # login_button.click()
    #
    # wrong_email_or_password = chromium_page.locator('[data-test="error"]')
    # expect(wrong_email_or_password).to_be_visible()
    # expect(wrong_email_or_password).to_have_text(
    #     'Epic sadface: Username and password do not match any user in this service')
