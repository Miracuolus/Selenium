import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/math.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    x_label = driver.find_element(By.ID, 'input_value')
    x = x_label.text
    y = calc(x)
    answer = driver.find_element(By.CLASS_NAME, 'form-control')
    answer.send_keys(y)
    check_box = driver.find_element(By.CSS_SELECTOR, 'label.form-check-label[for="robotCheckbox"]')
    check_box.click()
    radio_button = driver.find_element(By.CSS_SELECTOR, 'label.form-check-label[for="robotsRule"]')
    radio_button.click()
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()
