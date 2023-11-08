from pages.base_app import BasePage
from config.locators.locator_text_box import LocatorsTextBox as Loc
import config.input as data
from selenium.webdriver.support import expected_conditions as ec


class TextBox(BasePage):

    """Ввод данных в поля"""

    def enter_full_name(self) -> None:
        """Folder Full Name"""
        folder_name = self.wait.until(ec.visibility_of_element_located(Loc.LOCATOR_FIELD_FULL_NAME))
        folder_name.send_keys(data.full_name)

    def enter_email(self) -> None:
        """Folder Email"""
        folder_email = self.wait.until(ec.visibility_of_element_located(Loc.LOCATOR_FIELD_EMAIL))
        folder_email.send_keys(data.email)

    def enter_cur_address(self) -> None:
        """Folder Current Address"""
        folder_cur = self.wait.until(ec.visibility_of_element_located(Loc.LOCATOR_FIELD_CURRENT_ADDRESS))
        folder_cur.send_keys(data.cur_address)

    def enter_per_address(self) -> None:
        """Folder Permanent Address"""
        folder_per = self.wait.until(ec.visibility_of_element_located(Loc.LOCATOR_FIELD_PERMANENT_ADDRESS))
        folder_per.send_keys(data.per_address)

    def click_submit_btn(self) -> None:
        self.wait.until(ec.element_to_be_clickable(Loc.LOCATOR_BTN_SUBMIT)).click()

    def checks_enter_data(self) -> None:

        """Checking that the form is filled out correctly"""

        full_name = self.driver.find_element(*Loc.LOCATOR_FIELD_FULL_NAME).get_attribute("value")
        check_name = self.driver.find_element(*Loc.LOCATOR_CHECK_FORM_FULL_NAME).text.split(':')[-1].strip()
        assert full_name == check_name, f"Full Name {full_name} doesn't match, {check_name}"

        email = self.driver.find_element(*Loc.LOCATOR_FIELD_EMAIL).get_attribute("value")
        check_email = self.driver.find_element(*Loc.LOCATOR_CHECK_FORM_EMAIL).text.split(':')[-1].strip()
        assert email == check_email, f"Email {email} doesn't match, {check_email}"

        cur_address = self.driver.find_element(*Loc.LOCATOR_FIELD_CURRENT_ADDRESS).get_attribute("value")
        check_cur_address = self.driver.find_elements('id', 'currentAddress')[1].text.split(':')[-1].strip()
        assert cur_address == check_cur_address, f"Current Address {cur_address} doesn't match, {check_cur_address}"

        per_address = self.driver.find_element(*Loc.LOCATOR_FIELD_PERMANENT_ADDRESS).get_attribute("value")
        check_per_address = self.driver.find_elements('id', 'permanentAddress')[1].text.split(':')[-1].strip()
        assert per_address == check_per_address, f"Permanent Address {per_address} doesn't match, {check_per_address}"
