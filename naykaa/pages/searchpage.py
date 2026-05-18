import time

from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class SearchPage(BasePage):

    SEARCH_BOX = (
        By.XPATH,
        "//input[contains(@placeholder,'Search')]"
    )

    def search_product(self, product):

        self.enter_text(
            self.SEARCH_BOX,
            product
        )

        time.sleep(2)

        self.press_enter(
            self.SEARCH_BOX
        )