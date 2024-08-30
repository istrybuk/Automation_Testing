from selenium.webdriver.common.by import By
from page.base_page import BasePage

search_field_selector = (By.XPATH, '//*[@id="block-cleo-flex-mainnavigation"]/div[1]/ul/li[8]/div/form/input')
value_for_search_field = 'Blog'
search_from_page = (By.XPATH, '//*[@id="edit-query"]')


class HomePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.cleo.com/')

    # @property
    def search_field(self):
        return self.find(search_field_selector)

    # @property
    def search_field_is_displayed(self):
        return self.search_field().is_displayed()

    def submit_search_field(self):
        self.browser.find_element(*search_field_selector).submit()

    def send_value_in_search_field(self):
        send_search = self.browser.find_element(*search_field_selector)
        send_search.send_keys(value_for_search_field)

    def search_result(self):
        send_search_result = self.browser.find_element(*search_from_page)
        assert send_search_result.get_attribute('value') == value_for_search_field
