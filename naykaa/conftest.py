# import pytest
# from utilities.driver_setup import get_driver
#
# @pytest.fixture
# def driver():
#     driver = get_driver()
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")

    # Create driver only once
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.get("https://www.nykaa.com/")

    yield driver

    driver.quit()