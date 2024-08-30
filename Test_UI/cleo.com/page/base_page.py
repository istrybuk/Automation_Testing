import time

from datetime import datetime


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_elements(*args)

    def take_screenshot(self, nodeid):
        time.sleep(1)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.browser.save_screenshot(f'{nodeid}_{now}.png')
