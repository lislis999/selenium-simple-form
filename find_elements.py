from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for element in elements:
        element.send_keys("test")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # manage to copy a code for 30 seconds
    time.sleep(30)
    # close the browser
    browser.quit()

# dont forget to leave the empty line at the end of the file