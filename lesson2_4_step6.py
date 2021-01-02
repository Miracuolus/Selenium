import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/cats.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    verify = driver.find_element(By.ID, 'button').click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()