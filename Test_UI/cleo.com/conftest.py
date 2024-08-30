from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


@pytest.fixture()
def browser_mobile():
    mobile_emulation = {"deviceName": "Pixel 7"}  # Nexus 5
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    return browser
