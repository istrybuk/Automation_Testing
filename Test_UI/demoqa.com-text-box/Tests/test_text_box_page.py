import pytest
from config.links import Links
from pages.text_box_page import TextBox


@pytest.mark.smoke
def test_form_completion_check(browser):
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
