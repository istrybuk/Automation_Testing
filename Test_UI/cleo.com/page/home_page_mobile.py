from selenium.webdriver.common.by import By
from page.base_page import BasePage

value_for_search_field = 'Blog'
search_from_page = (By.XPATH, '//*[@id="edit-query"]')
menu_mobile = (By.XPATH, '//*[@id="block-cleo-flex-mainnavigation"]/div[2]/button/i[1]')
search_field_mobile = (By.XPATH, '//*[@id="block-cleo-flex-mainnavigation"]/div[1]/div/form/label/input')


class HomePageMobile(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.cleo.com/')

    def submit_search_field_mobile(self):
        self.browser.find_element(*search_field_mobile).submit()

    def search_result_mobile(self):
        send_search_result = self.browser.find_element(*search_from_page)
        assert send_search_result.get_attribute('value') == value_for_search_field

    def menu_mobile_click(self):
        menu_select = self.browser.find_element(*menu_mobile)
        menu_select.click()

    def search_menu_mobile(self):
        send_search = self.browser.find_element(*search_field_mobile)
        send_search.send_keys(value_for_search_field)
