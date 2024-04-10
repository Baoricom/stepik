from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    print(y)

    answer = browser.find_element(By.CSS_SELECTOR,'#answer')
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()


    radiobutton = browser.find_element(By.CSS_SELECTOR,'#robotsRule')
    radiobutton.click()

    submit = browser.find_element(By.XPATH,"//button[contains(text(),'Submit')]")
    submit.submit()

finally:

    time.sleep(10)

    browser.quit()