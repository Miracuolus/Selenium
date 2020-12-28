import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/registration2.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    first_name = driver.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    last_name.send_keys('Petrov')
    email = driver.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    email.send_keys('ex@mail.ru')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(1)
    message_el = driver.find_element(By.TAG_NAME, 'h1')
    message = message_el.text
    assert "Congratulations! You have successfully registered!" == message
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()