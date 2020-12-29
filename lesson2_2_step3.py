import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/selects1.html'
#link = 'http://suninjuly.github.io/selects2.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    num1 = driver.find_element(By.ID, 'num1')
    num2 = driver.find_element(By.ID, 'num2')
    answer = int(num1.text) + int(num2.text)
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(answer))
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()
