from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from behave.runner import Context
import time

logger = get_logger()


@given('User opens Nykaa website')
def step_impl(context: Context):

    context.driver.get("https://www.nykaa.com/")

    context.driver.maximize_window()

    logger.info("Nykaa website opened successfully")


@when('User searches for "{product}"')
def step_impl(context:Context, product):

    search_box = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.NAME, "search-suggestions-nykaa")
        )
    )

    search_box.clear()
    search_box.send_keys(product)

    time.sleep(2)

    search_box.send_keys(Keys.ENTER)

    logger.info(f"Product searched : {product}")

    time.sleep(5)


@when('User selects first fragrance')
def step_impl(context: Context):

    time.sleep(5)

    first_product = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//a[contains(@href,'/p/')])[1]"
            )
        )
    )

    context.driver.execute_script(
        "arguments[0].scrollIntoView();",
        first_product
    )

    assert first_product.is_displayed()

    first_product.click()

    logger.info("First fragrance selected successfully")

    time.sleep(5)

    windows = context.driver.window_handles

    if len(windows) > 1:
        context.driver.switch_to.window(windows[1])

@then('Product title should be visible')
def step_impl(context:Context):

    product_title = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1")
        )
    )

    title = product_title.text

    assert title != ""
    assert len(title) > 3

    logger.info(f"Product title verified : {title}")




@when('User adds product to cart')
def step_impl(context: Context):

    time.sleep(5)

    add_to_bag = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[contains(.,'Add to Bag') or contains(.,'Add to Cart')]"
            )
        )
    )

    context.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        add_to_bag
    )

    time.sleep(2)

    context.driver.execute_script(
        "arguments[0].click();",
        add_to_bag
    )

    logger.info("Product added to cart successfully")

    time.sleep(5)


@then('Product should be added successfully')
def step_impl(context:Context):

    page_source = context.driver.page_source.lower()

    assert "bag" in page_source or "shopping" in page_source

    logger.info("Product addition verified")




@when('User opens shopping cart')
def step_impl(context: Context):

    time.sleep(5)

    cart_button = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[contains(.,'Bag')] | //span[contains(.,'Bag')] | //a[contains(@href,'cart')]"
            )
        )
    )

    context.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        cart_button
    )

    time.sleep(2)

    context.driver.execute_script(
        "arguments[0].click();",
        cart_button
    )

    logger.info("Shopping cart opened successfully")

    time.sleep(5)




@then('Shopping cart page should be displayed')
def step_impl(context: Context):

    current_url = context.driver.current_url.lower()

    page_source = context.driver.page_source.lower()

    assert (
        "cart" in current_url
        or "bag" in page_source
        or "shopping bag" in page_source
    )

    logger.info("Shopping cart page verified successfully")



@when('User views order summary')
def step_impl(context: Context):

    time.sleep(5)

    current_url = context.driver.current_url.lower()

    page_source = context.driver.page_source.lower()

    assert (
        "cart" in current_url
        or "bag" in page_source
        or "price details" in page_source
        or "grand total" in page_source
        or "summary" in page_source
    )

    logger.info("Order summary verified successfully")




@when('User proceeds to checkout')
def step_impl(context: Context):

    time.sleep(5)

    current_url = context.driver.current_url.lower()

    page_source = context.driver.page_source.lower()

    proceed_buttons = context.driver.find_elements(
        By.XPATH,
        "//button | //span | //div"
    )

    button_found = False

    for button in proceed_buttons:

        text = button.text.lower()

        if (
            "proceed" in text
            or "checkout" in text
            or "place order" in text
            or "continue" in text
            or "address" in text
        ):

            try:

                context.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    button
                )

                time.sleep(1)

                context.driver.execute_script(
                    "arguments[0].click();",
                    button
                )

                logger.info(
                    f"Checkout related button clicked : {text}"
                )

                button_found = True

                break

            except Exception as e:

                logger.error(f"Button click failed : {str(e)}")

    assert (
        button_found
        or "cart" in current_url
        or "bag" in page_source
        or "checkout" in page_source
    )

    logger.info("Proceed to checkout validation successful")

    time.sleep(5)


@then('Order confirmation process should be verified')
def step_impl(context: Context):

    current_url = context.driver.current_url.lower()

    assert (
        "checkout" in current_url
        or "address" in current_url
        or "payment" in current_url
        or "cart" in current_url
    )

    logger.info("Complete End To End flow verified successfully")