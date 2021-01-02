import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/wait1.html'
try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    verify = driver.find_element(By.CSS_SELECTOR , 'button#verify.btn.btn-primary').click()
    message = driver.find_element(By.CSS_SELECTOR , 'div#verify_message.container').text
    assert message == 'Verification was successful!'
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    driver.quit()