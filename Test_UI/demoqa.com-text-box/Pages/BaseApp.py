from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self, driver, url,):# timeout=10):
        self.driver = driver
        self.url = url
        # self.browser.implicitly_wait(timeout)
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    """Открытие страницы"""
    def open(self):
        self.driver.get(self.url)
