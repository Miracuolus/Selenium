import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestAbs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_reg1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.driver.get(link)
        first_input = self.driver.find_element(By.CSS_SELECTOR, 'div.form-group.first_class input.form-control.first[placeholder="Input your first name"]').send_keys('Ivan')
        last_input = self.driver.find_element(By.CSS_SELECTOR, 'div.form-group.second_class input.form-control.second[placeholder="Input your last name"]').send_keys('Petrov')
        email = self.driver.find_element(By.CSS_SELECTOR, 'div.form-group.third_class input.form-control.third[placeholder="Input your email"]').send_keys('ex@mail.ru')
        button = self.driver.find_element(By.TAG_NAME, 'button')
        button.click()
        time.sleep(1)
        message_el = self.driver.find_element(By.TAG_NAME, 'h1')
        message = message_el.text
        self.assertEqual(message, "Congratulations! You have successfully registered!", "Should be absolute equal")

    def test_reg2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        self.driver.get(link)
        first_input = self.driver.find_element(By.CSS_SELECTOR, 'div.form-group.first_class input.form-control.first[placeholder="Input your first name"]').send_keys('Ivan')
        last_input = self.driver.find_element(By.CSS_SELECTOR, 'div.form-group.second_class input.form-control.second[placeholder="Input your last name"]').send_keys('Petrov')
        email = self.driver.find_element(By.CSS_SELECTOR, 'div.form-group.third_class input.form-control.third[placeholder="Input your email"]').send_keys('ex@mail.ru')
        button = self.driver.find_element(By.TAG_NAME, 'button')
        button.click()
        time.sleep(1)
        message_el = self.driver.find_element(By.TAG_NAME, 'h1')
        message = message_el.text
        self.assertEqual(message, "Congratulations! You have successfully registered!", "Should be absolute equal")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
