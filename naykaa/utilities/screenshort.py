import os
import time

def capture_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    file_name = f"screenshots/{name}_{int(time.time())}.png"
    driver.save_screenshot(file_name)
    return file_name