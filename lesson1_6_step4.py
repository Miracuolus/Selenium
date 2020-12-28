import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/simple_form_find_task.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    #first_name = driver.find_element(By.NAME, 'first_name')
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