import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/huge_form.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('ivan')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()