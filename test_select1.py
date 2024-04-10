from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
#


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID,'num2').text
    num3 = str(str(int(x)+int(y)))
    print(num3)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(num3)

    browser.find_element(By.XPATH,"//button[contains(text(),'Submit')]").click()

finally:

    time.sleep(3)

    browser.quit()