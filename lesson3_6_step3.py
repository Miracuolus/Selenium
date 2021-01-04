import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()


links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'
         ]


@pytest.mark.parametrize('links', links)
def test_find_message(browser, links):
    browser.get(links)
    browser.find_element(By.CSS_SELECTOR, '.textarea').send_keys(
        str(math.log(int(time.time()))))
    browser.find_element_by_css_selector("button.submit-submission").click()
    text = browser.find_element_by_tag_name("pre").text
    assert text == 'Correct!', f'Should be "Correct" instead "{text}"'
