import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
    book = driver.find_element(By.TAG_NAME, 'button').click()
    x = driver.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    input_tag = driver.find_element(By.CSS_SELECTOR, 'input.form-control#answer').send_keys(calc(x))
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary#solve').click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()