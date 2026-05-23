from utils.driver_factory import get_driver
from utils.screenshot import capture_screenshot
import allure
import logging
from datetime import datetime


logging.basicConfig(
    filename="logs/test_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def before_scenario(context, scenario):

    context.driver = get_driver()

    logging.info(f"STARTED SCENARIO : {scenario.name}")


def after_step(context, step):

    screenshot_path = capture_screenshot(
        context.driver,
        f"{step.name}_{datetime.now().strftime('%H%M%S')}"
    )

    with open(screenshot_path, "rb") as file:

        allure.attach(
            file.read(),
            name=step.name,
            attachment_type=allure.attachment_type.PNG
        )

    logging.info(f"STEP EXECUTED : {step.name}")
    logging.info(f"SCREENSHOT SAVED : {screenshot_path}")


def after_scenario(context, scenario):

    logging.info(f"ENDED SCENARIO : {scenario.name}")

    context.driver.quit()