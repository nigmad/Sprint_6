import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть на Яндекс Лого')
    def click_on_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Кликнуть на Самокат Лого')
    def click_on_samokat_logo(self):
        self.click_on_element(MainPageLocators.SAMOKAT_LOGO)


    @allure.step('Кликнуть на кнопку Заказать внизу страницы')
    def click_on_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Кликнуть на кнопку Заказать вверху страницы')
    def click_on_top_order_button(self):
        self.click_on_element(MainPageLocators.TOP_ORDER_BUTTON)
