from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_TITLE = (
        By.XPATH,
        "//*[contains(text(),'Shopping Bag')]"
    )

    def verify_cart(self):
        return self.is_displayed(self.CART_TITLE)