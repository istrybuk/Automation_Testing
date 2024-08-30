from page.home_page import HomePage
from page.home_page_mobile import HomePageMobile


def test_search_field_is_disp(browser):
    home_pag = HomePage(browser)
    home_pag.open()
    home_pag.send_value_in_search_field()
    home_pag.take_screenshot('value')
    home_pag.submit_search_field()
    home_pag.search_result()
    home_pag.take_screenshot('value_True')


def test_search_field_is_disp_mob(browser_mobile):
    home_pag = HomePageMobile(browser_mobile)
    home_pag.open()
    home_pag.menu_mobile_click()
    home_pag.search_menu_mobile()
    home_pag.take_screenshot("mobile_value")
    home_pag.submit_search_field_mobile()
    home_pag.search_result_mobile()
    home_pag.take_screenshot('mobile_value_True')
