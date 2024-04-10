from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME,'trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID,'input_value').text
    browser.find_element(By.ID,'answer').send_keys(calc(x))
    browser.find_element(By.TAG_NAME,'button').click()

finally:

    time.sleep(10)

    browser.quit()

