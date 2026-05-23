from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FragrancePage(BasePage):

    FIRST_PRODUCT = (
        By.XPATH,
        "(//div[contains(@class,'css-xrzmfa')])[1]"
    )

    PRODUCT_TITLE = (
        By.XPATH,
        "//h1"
    )

    ADD_TO_BAG = (
        By.XPATH,
        "//button[contains(text(),'Add to Bag')]"
    )

    BAG_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'css-g4vs13')]"
    )

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart(self):
        self.click(self.ADD_TO_BAG)