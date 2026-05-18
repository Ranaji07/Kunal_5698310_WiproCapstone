from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class LoginPage(BasePage):

    SIGNIN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign in')]")

    MOBILE_INPUT = (By.XPATH, "//input[@type='tel']")

    CONTINUE_BUTTON = (By.XPATH, "//button[@type='submit']")

    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Please enter valid mobile number')]")

    def open_login_popup(self):
        self.click(self.SIGNIN_BUTTON)

    def enter_mobile_number(self, mobile):
        self.enter_text(self.MOBILE_INPUT, mobile)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)