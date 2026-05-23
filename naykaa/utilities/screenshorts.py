import os
import time

def capture_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    screenshots = f"screenshots/{name}_{int(time.time())}.png"
    driver.save_screenshot(screenshots)
    return screenshots
