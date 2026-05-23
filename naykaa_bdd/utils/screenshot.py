import os
import re
from datetime import datetime


def capture_screenshot(driver, name):

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    safe_name = re.sub(r'[<>:"/\\\\|?*]', '', name)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = f"screenshots/{safe_name}_{timestamp}.png"

    driver.save_screenshot(path)

    return path