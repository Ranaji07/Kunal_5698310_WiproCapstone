from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    SEARCH_BOX = (By.NAME, "search-suggestions-nykaa")

    def open_website(self):
        self.driver.get("https://www.nykaa.com/")

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)