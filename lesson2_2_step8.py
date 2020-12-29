import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Hello world!.txt')  
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    first_name = driver.find_element(By.NAME, 'firstname')
    first_name.send_keys('Иван')
    last_name = driver.find_element(By.NAME, 'lastname')
    last_name.send_keys('Иванов')
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('ivanov@mail.ru')
    file_load = driver.find_element(By.NAME, 'file')
    file_load.send_keys(file_path)
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(8)
    driver.quit()
