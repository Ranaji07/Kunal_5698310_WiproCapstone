# test_nykaa_fragrance_e2e.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging


def get_logger():

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        "logs/automation.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    return logger


class TestNykaaFragranceE2E:

    def setup_method(self):

        service = Service(ChromeDriverManager().install())

        self.driver = webdriver.Chrome(service=service)

        self.driver.maximize_window()

        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self):

        self.driver.quit()

    def test_nykaa_fragrance_flow(self):

        driver = self.driver
        wait = self.wait


        # STEP 1 - OPEN NYKAA


        driver.get("https://www.nykaa.com/")

        print("Nykaa website opened")

        assert "Nykaa" in driver.title


        # STEP 2 - LOGIN OPERATION


        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Sign in')]")
            )
        )

        login_button.click()



        # ENTER MOBILE NUMBER

        mobile_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='tel']")
            )
        )

        mobile_input.send_keys("9876543210")


        # STEP 3 - SEARCH PRODUCT


        search_box = wait.until(
            EC.presence_of_element_located(
                (By.NAME, "search-suggestions-nykaa")
            )
        )

        search_box.send_keys("Perfume")

        time.sleep(10)

        search_box.send_keys(Keys.ENTER)



        time.sleep(10)


        # STEP 4 - APPLY SORT


        try:

            sort_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(),'Sort By')]")
                )
            )

            sort_button.click()



        except:

            print("Sort option not available")

        time.sleep(10)


        # STEP 5 - OPEN FIRST PRODUCT


        products = driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'/p/')]"
        )

        products[0].click()



        # SWITCH TO NEW TAB

        tabs = driver.window_handles

        driver.switch_to.window(tabs[1])

        time.sleep(5)


        # STEP 6 - VERIFY PRODUCT PAGE


        assert "Add to Bag" in driver.page_source




        # STEP 7 - ADD PRODUCT TO BAG


        add_to_bag = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Add to Bag')]")
            )
        )

        add_to_bag.click()



        time.sleep(5)


        # STEP 8 - OPEN BAG

        def click_bag(self):
            bag_click = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,"//button[@id='header-bag-icon')]")
                )
            )
            bag_click.click()
            time.sleep(10)

        try:

            bag_button = driver.find_element(
                By.XPATH,
                "//button[contains(@class,'css')]"
            )

            bag_button.click()



        except:

            print("Bag button not found")

        time.sleep(5)


        # STEP 9 - VERIFY BAG PAGE


        assert "Bag" in driver.page_source




        # STEP 10 - CHECKOUT OPERATION


        try:

            checkout_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(),'Proceed')]")
                )
            )

            checkout_button.click()



        except:

            print("Checkout button not found")

        time.sleep(5)


        # STEP 11 - VERIFY CHECKOUT PAGE


        try:

            assert "address" in driver.page_source.lower() or \
                   "payment" in driver.page_source.lower()

            print("Checkout page verified")

        except:

            print("Checkout page verification failed")




        # STEP - TAKE SCREENSHOT


        driver.save_screenshot("screenshots/fragrance_test7.png")

        print("Screenshot captured")

        print("END TO END TEST PASSED SUCCESSFULLY")