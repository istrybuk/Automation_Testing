import pytest
from Config.locators import *
from Pages.TextBoxPage import TextBox


@pytest.mark.parametrize("test", [f"test-{i}" for i in range(1, 2)])
def test_form_completion_check(browser, test):
    browser = browser
    link = Links.TEXT_BOX_PAGE
    page_text_box = TextBox(browser, link)
    page_text_box.open()
    page_text_box.enter_full_name()
    page_text_box.enter_email()
    page_text_box.enter_cur_address()
    page_text_box.enter_per_address()
    page_text_box.click_submit_btn()
    page_text_box.checks_enter_data()
