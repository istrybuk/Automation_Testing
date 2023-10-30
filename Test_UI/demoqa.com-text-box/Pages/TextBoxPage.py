import allure
from selenium.webdriver import ActionChains
from Pages.BaseApp import BasePage
import Config.locators as loc
import Config.input as data


class TextBox(BasePage):

    """Ввод данных в поля"""

    @allure.step("Enter full name")
    def enter_full_name(self):
        """Folder Full Name"""
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_FULL_NAME).send_keys(data.full_name)

    @allure.step("Enter Email")
    def enter_email(self):
        """Folder Email"""
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_EMAIL).send_keys(data.email)

    @allure.step("Enter Current Address")
    def enter_cur_address(self):
        """Folder Current Address"""
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_CURRENT_ADDRESS).send_keys(data.cur_address)

    @allure.step("Enter Permanent Address")
    def enter_per_address(self):
        """Folder Permanent Address"""
        self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_PERMANENT_ADDRESS).send_keys(data.per_address)

    @allure.step("Click Submit")
    def click_submit_btn(self):
        action = ActionChains(self.driver)
        button_submit = self.driver.find_element(*loc.PageTextBox.LOCATOR_BTN_SUBMIT)
        action.move_to_element(button_submit).click(button_submit).perform()
        # self.driver.find_element('id', 'submit').click()

    @allure.step("Field entry checks")
    def checks_enter_data(self):

        """Checking that the form is filled out correctly"""

        full_name = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_FULL_NAME).get_attribute("value")
        check_name = self.driver.find_element(*loc.PageTextBox.LOCATOR_CHECK_FORM_FULL_NAME).text.split(':')[-1].strip()
        assert full_name == check_name, f"Full Name {full_name} doesn't match, {check_name}"

        email = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_EMAIL).get_attribute("value")
        check_email = self.driver.find_element(*loc.PageTextBox.LOCATOR_CHECK_FORM_EMAIL).text.split(':')[-1].strip()
        assert email == check_email, f"Email {email} doesn't match, {check_email}"

        cur_address = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_CURRENT_ADDRESS).get_attribute("value")
        check_cur_address = self.driver.find_elements('id', 'currentAddress')[1].text.split(':')[-1].strip()
        assert cur_address == check_cur_address, f"Current Address {cur_address} doesn't match, {check_cur_address}"

        per_address = self.driver.find_element(*loc.PageTextBox.LOCATOR_FIELD_PERMANENT_ADDRESS).get_attribute("value")
        check_per_address = self.driver.find_elements('id', 'permanentAddress')[1].text.split(':')[-1].strip()
        assert per_address == check_per_address, f"Permanent Address {per_address} doesn't match, {check_per_address}"
