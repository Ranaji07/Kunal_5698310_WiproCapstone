from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave.runner import Context
from utils.logger import get_logger
import time

logger = get_logger()


@when('User searches fragrance product "{product}"')
def step_impl(context: Context, product):

    search_box = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.NAME, "search-suggestions-nykaa")
        )
    )

    search_box.clear()

    search_box.send_keys(product)

    time.sleep(2)

    # Initiate Search
    search_box.send_keys(Keys.ENTER)

    logger.info(f"Search initiated for : {product}")

    context.product = product

    time.sleep(5)


@then('Search results should appear')
def step_impl(context: Context):

    products = WebDriverWait(context.driver, 30).until(
        EC.presence_of_all_elements_located(
            (
                By.XPATH,
                "//a[contains(@href,'/p/')]"
            )
        )
    )

    assert len(products) > 0

    logger.info(
        f"Search results validated successfully for {context.product}"
    )


@then('Invalid search message should appear')
def step_impl(context: Context):

    page_source = context.driver.page_source.lower()

    assert (
        "no results" in page_source
        or "sorry" in page_source
        or "not found" in page_source
    )

    logger.info(
        f"Invalid search validated successfully for {context.product}"
    )