import pytest
from Config.locators import *
from Pages.TextBoxPage import TextBox

@pytest.mark.parametrize("test", [f"test-{i}" for i in range(1, 2)])
# @pytest.mark.smoke
def test_buy_phone_payment_6_months(browser, test):
    browser = browser
    link = Links.TEXT_BOX_PAGE
    PageTextBox = TextBox(browser, link)
    PageTextBox.open()
    PageTextBox.enter_full_name()
    PageTextBox.enter_email()
    PageTextBox.enter_cur_address()
    PageTextBox.enter_per_address()
    PageTextBox.click_submit_btn()
    PageTextBox.checks_enter_data()