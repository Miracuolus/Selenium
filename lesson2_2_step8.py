import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/file_input.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    first_name = driver.find_element(By.NAME, 'firstname')
    x = x_label.text
    #driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    driver.execute_script("window.scrollBy(0, 100);")
    answer = driver.find_element(By.CLASS_NAME, 'form-control')
    answer.send_keys(calc(x))
    check_box = driver.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    radio_button = driver.find_element(By.ID, 'robotsRule').click()
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()
