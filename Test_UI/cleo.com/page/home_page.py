from selenium.webdriver.common.by import By

from page.base_page import BasePage

search_field_selector = (By.XPATH, '//*[@id="block-cleo-flex-mainnavigation"]/div[1]/ul/li[8]/div/form/input')

menu_home_selector = (By.XPATH, '//*[@id="block-cleo-flex-mainnavigation"]/div[2]/button/i[1]')


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.cleo.com/')

    def search_field(self):
        return self.find(search_field_selector)

    def home_menu(self):
        return self.find(menu_home_selector)

    def search_field_is_displayed(self):
        return self.search_field().is_displayed()
