from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.wrong_email_or_password = page.locator('[data-test="error"]')


    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password).to_be_visible()
        expect(self.wrong_email_or_password).to_have_text('Epic sadface: Username and password do not match any user in this service')

