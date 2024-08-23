from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill in the required fields
    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys("Elizaveta")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys("Lysenko")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys("test@mail.com")

    # Submit the form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Wait for the page to load
    time.sleep(1)

    # Find the element with the text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Check that the expected text matches the text on the website
    assert "Congratulations! You have successfully registered!" == welcome_text

    print("Test Passed: Registration was successful!")

except AssertionError as e:
    print(f"Test Failed: {e}")

finally:
    # Wait to visually assess the script results
    time.sleep(5)
    # Close the browser
    browser.quit()
