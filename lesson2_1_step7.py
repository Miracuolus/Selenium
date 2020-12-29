import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/get_attribute.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    image = driver.find_element(By.ID, 'treasure')
    x = image.get_attribute('valuex')
    y = calc(x)
    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(y)
    check_box = driver.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    radio_button = driver.find_element(By.ID, 'robotsRule')
    radio_button.click()
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()
