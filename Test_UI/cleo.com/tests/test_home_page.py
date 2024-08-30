from page.base_page import BasePage
from page.home_page import HomePage
from page.search_page import SearchPage


def test_proba(browser):
    home_page = HomePage(browser)
    home_page.open()
    assert home_page.search_field_is_displayed()


