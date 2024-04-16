import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_registration1(self):
        self.driver.get("https://suninjuly.github.io/registration1.html")

        first_name_input = self.driver.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        first_name_input.send_keys("Your First Name")

        last_name_input = self.driver.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        last_name_input.send_keys("Your Last Name")

        email_input = self.driver.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        email_input.send_keys("your_email@example.com")

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
        submit_button.click()

        time.sleep(2)

        result_message = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(result_message, "Congratulations! You have successfully registered!")

    def test_registration2(self):
        self.driver.get("https://suninjuly.github.io/registration2.html")

        first_name_input = self.driver.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        first_name_input.send_keys("Your First Name")

        last_name_input = self.driver.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        last_name_input.send_keys("Your Last Name")

        email_input = self.driver.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        email_input.send_keys("your_email@example.com")

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
        submit_button.click()

        time.sleep(2)

        result_message = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(result_message, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
