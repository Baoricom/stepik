from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    pric = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.ID,'input_value').text
    browser.find_element(By.ID,'answer').send_keys(calc(x))
    browser.find_element(By.ID,'solve').click()

finally:

    time.sleep(10)

    browser.quit()

