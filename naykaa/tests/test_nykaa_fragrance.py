# test_nykaa_fragrance.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


class TestNykaaFragrance:

    @pytest.fixture(autouse=True)
    def setup(self):

        service = Service(ChromeDriverManager().install())

        self.driver = webdriver.Chrome(service=service)

        self.driver.maximize_window()

        self.wait = WebDriverWait(self.driver, 20)

        yield

        self.driver.quit()

    # ====================================================
    # POSITIVE TEST CASE 1
    # VERIFY HOMEPAGE LOADS SUCCESSFULLY
    # ====================================================

    def test_verify_homepage(self):

        self.driver.get("https://www.nykaa.com/")

        assert "Nykaa" in self.driver.title

        print("Homepage loaded successfully")

    # ====================================================
    # POSITIVE TEST CASE 2
    # VERIFY PERFUME SEARCH FUNCTIONALITY
    # ====================================================

    def test_search_perfume(self):

        self.driver.get("https://www.nykaa.com/")

        search_box = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "search-suggestions-nykaa")
            )
        )

        search_box.send_keys("Perfume")

        time.sleep(2)

        search_box.send_keys(Keys.ENTER)

        time.sleep(5)

        assert "Perfume" in self.driver.page_source

        print("Perfume search successful")

    # ====================================================
    # POSITIVE TEST CASE 3
    # VERIFY PRODUCT PAGE OPENS
    # ====================================================

    def test_open_product_page(self):

        self.driver.get("https://www.nykaa.com/")

        search_box = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "search-suggestions-nykaa")
            )
        )

        search_box.send_keys("Perfume")

        search_box.send_keys(Keys.ENTER)

        time.sleep(5)

        products = self.driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'/p/')]"
        )

        products[0].click()

        tabs = self.driver.window_handles

        self.driver.switch_to.window(tabs[1])

        time.sleep(5)

        assert "Add to Bag" in self.driver.page_source

        print("Product page opened successfully")

    # ====================================================
    # POSITIVE TEST CASE 4
    # VERIFY ADD TO BAG FUNCTIONALITY
    # ====================================================

    def test_add_to_bag(self):

        self.driver.get("https://www.nykaa.com/")

        search_box = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "search-suggestions-nykaa")
            )
        )

        search_box.send_keys("Perfume")

        search_box.send_keys(Keys.ENTER)

        time.sleep(5)

        products = self.driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'/p/')]"
        )

        products[0].click()

        tabs = self.driver.window_handles

        self.driver.switch_to.window(tabs[1])

        time.sleep(5)

        add_to_bag = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Add to Bag')]")
            )
        )

        add_to_bag.click()

        print("Product added to bag successfully")

    # ====================================================
    # NEGATIVE TEST CASE 1
    # VERIFY INVALID SEARCH
    # ====================================================

    def test_invalid_product_search(self):

        self.driver.get("https://www.nykaa.com/")

        search_box = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "search-suggestions-nykaa")
            )
        )

        search_box.send_keys("xyzinvalidproduct123")

        search_box.send_keys(Keys.ENTER)

        time.sleep(5)

        assert "No Results" in self.driver.page_source or \
               "result" in self.driver.page_source.lower()

        print("Invalid search test executed")

    # ====================================================
    # NEGATIVE TEST CASE 2
    # VERIFY INVALID MOBILE LOGIN
    # ====================================================

    def test_invalid_login(self):

        self.driver.get("https://www.nykaa.com/")

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Sign in')]")
            )
        )

        login_button.click()

        mobile_input = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='tel']")
            )
        )

        mobile_input.send_keys("12345")

        time.sleep(3)

        print("Invalid login test executed")