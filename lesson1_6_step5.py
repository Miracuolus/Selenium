import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/find_link_text'
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    link = driver.find_element(By.LINK_TEXT, link_text)
    link.click()
    first_name = driver.find_element(By.TAG_NAME, 'input')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.NAME, 'last_name')
    last_name.send_keys('Petrov')
    city = driver.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Smolensk')
    country = driver.find_element(By.ID, 'country')
    country.send_keys('Russia')
    button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()
