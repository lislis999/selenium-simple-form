from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/find_link_text"
inside_link= str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    search1 = browser.find_element(By.LINK_TEXT, inside_link)
    search1.click()

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
    # close the browser
    time.sleep(30)
    browser.quit()

# dont forget to leave the empty line at the end of the file
