from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url , "Substring 'login' is not present in current browser url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "There is no login form on the page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
         assert self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER), "There is no login form on the page"