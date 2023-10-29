# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from Pages.BaseApp import BasePage
# from Config.Locators.locators import *
import Config.locators as loc
import Config.input as data


class TextBox(BasePage):
    """Represent text-box page web element locators."""

    LOCATOR_FIELD_FULL_NAME = ('id', 'userName')
    LOCATOR_FIELD_EMAIL = ('id', 'userEmail')
    LOCATOR_FIELD_CURRENT_ADDRESS = ('id', 'currentAddress')
    LOCATOR_FIELD_PERMANENT_ADDRESS = ('id', 'permanentAddress')
    LOCATOR_BTN_SUBMIT = ('id', 'submit')
    LOCATOR_CHECK_FORM_FULL_NAME = ('id', 'name')
    LOCATOR_CHECK_FORM_EMAIL = ('id', 'email')
    LOCATOR_CHECK_FORM_CURRENT_ADDRESS = ('id', 'currentAddress')
    LOCATOR_CHECK_FORM_PERMANENT_ADDRESS = ('id', 'permanentAddress')

    """Ввод данных в поля"""
    def enter_full_name(self):
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_FULL_NAME).send_keys(data.full_name)

    def enter_email(self):
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_EMAIL).send_keys(data.email)

    def enter_cur_address(self):
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_CURRENT_ADDRESS).send_keys(data.cur_address)

    def enter_per_address(self):
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_PERMANENT_ADDRESS).send_keys(data.per_address)

    def click_submit_btn(self):
        action = ActionChains(self.driver)
        button_submit = self.driver.find_element(*loc.PageTextBox.LOCATOR_BTN_SUBMIT)
        action.move_to_element(button_submit).click(button_submit).perform()
        # self.driver.find_element('id', 'submit').click()


    def checks_enter_data(self):
        """Поле проверка адреса"""
        full_name = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_FULL_NAME).get_attribute("value")
        check_full_name = self.driver.find_element(*loc.PageTextBox.LOCATOR_CHECK_FORM_FULL_NAME).text.split(':')[-1].strip()
        assert full_name == check_full_name, f"Full Name {full_name} doesn't match, {check_full_name}"

        email = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_EMAIL).get_attribute("value")
        check_email = self.driver.find_element(*loc.PageTextBox.LOCATOR_CHECK_FORM_EMAIL).text.split(':')[-1].strip()
        assert email == check_email, f"Email {email} doesn't match, {check_email}"

        cur_address = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_CURRENT_ADDRESS).get_attribute("value")
        check_cur_address = self.driver.find_elements('id', 'currentAddress')[1].text.split(':')[-1].strip()
        assert cur_address == check_cur_address, f"Current Address {cur_address} doesn't match, {check_cur_address}"

        per_address = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_PERMANENT_ADDRESS).get_attribute("value")
        check_per_address = self.driver.find_elements('id', 'permanentAddress')[1].text.split(':')[-1].strip()
        assert per_address == check_per_address, f"Permanent Address {per_address} doesn't match, {check_per_address}"



