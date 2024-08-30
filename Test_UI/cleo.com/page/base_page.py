class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, *args):
        return self.browser.browser.find_element(*args)
