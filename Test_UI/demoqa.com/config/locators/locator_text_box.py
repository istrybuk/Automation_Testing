from selenium.webdriver.common.by import By


class LocatorsTextBox:
    """Represent text-box page web element locators."""

    LOCATOR_FIELD_FULL_NAME = (By.ID, 'userName')
    LOCATOR_FIELD_EMAIL = (By.ID, 'userEmail')
    LOCATOR_FIELD_CURRENT_ADDRESS = (By.ID, 'currentAddress')
    LOCATOR_FIELD_PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
    LOCATOR_BTN_SUBMIT = (By.ID, 'submit')
    LOCATOR_CHECK_FORM_FULL_NAME = (By.ID, 'name')
    LOCATOR_CHECK_FORM_EMAIL = (By.ID, 'email')
    LOCATOR_CHECK_FORM_CURRENT_ADDRESS = (By.ID, 'currentAddress')
    LOCATOR_CHECK_FORM_PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
