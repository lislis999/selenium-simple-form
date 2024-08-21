from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Elizaveta")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Lysenko")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.city')
    input3.send_keys("Berlin")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Germany")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # manage to copy a code for 30 seconds
    time.sleep(30)
    # close the browser
    browser.quit()

# dont forget to leave the empty line at the end of the file
