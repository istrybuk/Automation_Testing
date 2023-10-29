from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        """Открытие страницы"""
        self.driver.get(self.url)
