import allure

from project_url import Curl
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage



class TestRedirectYandexLogo:
    @allure.title("Проверка редиректа при клике на логотип Яндекс")
    def test_redirect_yandex_logo(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_yandex_logo()
        main_page.wait_for_number_of_windows(2)
        main_page.switch_to_new_window()
        main_page.wait_for_url_contains(Curl.AUTH_YANDEX)
        main_page.wait_for_url_contains(Curl.DZEN_SITE)

        assert Curl.DZEN_SITE in main_page.get_current_url()



class TestRedirectSamokatLogo:
    @allure.title("Проверка редиректа при клике на логотип Самоката")
    def test_redirect_samokat_logo(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_top_order_button()
        main_page.click_on_samokat_logo()
        main_page.wait_for_element(MainPageLocators.SAMOKAT_HOME_HEADER)

        assert main_page.get_current_url().startswith(Curl.main_site) and main_page.get_current_url().endswith('/')