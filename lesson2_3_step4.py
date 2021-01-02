import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    button = driver.find_element(By.TAG_NAME, 'button').click()
    confirm = driver.switch_to.alert.accept()
    x = driver.find_element(By.ID, 'input_value').text
    input_tag = driver.find_element(By.TAG_NAME, 'input').send_keys(calc(x))
    button = driver.find_element(By.TAG_NAME, 'button').click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()