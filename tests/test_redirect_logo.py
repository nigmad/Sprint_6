import pytest
import allure

from project_url import Curl
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.base_page import BasePage


class TestRedirectYandexLogo:
    @allure.title("Проверка редиректа при клике на логотип Яндекс")
    def test_redirect_yandex_logo(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        main_page.click_on_yandex_logo()
        base_page.wait_for_number_of_windows(2)
        base_page.switch_to_new_window()
        base_page.wait_for_url_contains("passport.yandex.ru")
        base_page.wait_for_url_contains("dzen.ru")

        assert "dzen.ru" in driver.current_url



    class TestRedirectSamokatLogo:
        @allure.title("Проверка редиректа при клике на логотип Самоката")
        def test_redirect_samokat_logo(self, driver):
            main_page = MainPage(driver)
            base_page = BasePage(driver)

            main_page.click_on_top_order_button()
            main_page.click_on_samokat_logo()
            base_page.wait_for_element(MainPageLocators.SAMOKAT_HOME_HEADER)

            assert driver.current_url.startswith(Curl.main_site) and driver.current_url.endswith('/')
