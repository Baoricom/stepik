import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration_success(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Find and fill out the first name input
        first_name_input = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        first_name_input.send_keys("Your First Name")

        # Find and fill out the last name input
        last_name_input = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        last_name_input.send_keys("Your Last Name")

        # Find and fill out the email input
        email_input = self.browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        email_input.send_keys("your_email@example.com")
        time.sleep(5)
        # Submit the form
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Wait for the page to load
        time.sleep(1)

        # Find and assert the welcome text
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
