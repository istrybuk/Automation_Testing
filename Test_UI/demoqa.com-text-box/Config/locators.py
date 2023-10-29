class PageTextBox:
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


class Links:

    HOST = "https://demoqa.com/"
    TEXT_BOX_PAGE = f"{HOST}text-box"
