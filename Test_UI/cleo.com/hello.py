import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # browser = webdriver.Chrome(options=chrome_options)

    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser


def test_open(browser):
    browser.get('https://www.cleo.com/')
    field_search = browser.find_element(By.XPATH,
                                        '//*[@id="block-cleo-flex-mainnavigation"]/div[1]/ul/li[8]/div/form/input')
    assert field_search.is_displayed()
    field_search.send_keys('Blog')
    # assert field_search.text == 'Hello'
    field_search.submit()

    search_from_page = browser.find_element(By.XPATH, '//*[@id="edit-query"]').get_attribute('value')
    assert search_from_page == 'Blog'

    time.sleep(10)
