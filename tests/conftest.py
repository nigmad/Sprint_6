import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


from project_url import *
from pages.main_page import MainPage
from pages.order_page import OrderPage



@pytest.fixture(scope='function')
def driver():
    options = FirefoxOptions()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Firefox(options = options)
    driver.get(Curl.main_site)
    yield driver
    driver.quit()

@pytest.fixture
def open_order_site_top_button(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    main_page.click_on_top_order_button()

    order_page.wait_for_name_field()

    return OrderPage(driver)


@pytest.fixture
def open_order_site_bottom_button(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.click_on_bottom_order_button()

    order_page.wait_for_name_field()

    return OrderPage(driver)


