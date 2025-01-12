import allure

from locators.confirmation_order_window_locators import ConfirmationOrderWindowLocators
from locators.succesfull_order_page_locators import SuccessfulOrderPageLocators
from pages.base_page import BasePage
from locators.order_form_locators import OrderFormLocators


class OrderPage(BasePage):


    @allure.step("Заполнить форму Для кого самокат")
    def fill_user_data_order_form(self, name, surname, address, phone):
        self.send_keys_to_input(OrderFormLocators.NAME, name)
        self.send_keys_to_input(OrderFormLocators.SURNAME, surname)
        self.send_keys_to_input(OrderFormLocators.ADDRESS, address)
        self.send_keys_to_input(OrderFormLocators.PHONE, phone)

    @allure.step("Выбрать станцию метро")
    def select_metro_station(self, metro_station_locator):
        self.click_on_element(OrderFormLocators.METRO_STATION_FIELD)
        self.scroll_to_element(metro_station_locator)
        self.click_on_element(metro_station_locator)

    @allure.step("Нажать на кнопку Далее")
    def click_next_button(self):
        self.click_on_element(OrderFormLocators.NEXT_BUTTON)
        self.wait_for_element(OrderFormLocators.ABOUT_ORDER_HEADER)

    @allure.step("Выбрать дату заказа")
    def select_order_date(self, order_date_locators):
        self.click_on_element(OrderFormLocators.WHEN_DELIVER_SCOOTER_FIELD)
        self.scroll_to_element(order_date_locators)
        self.click_on_element(order_date_locators)

    @allure.step("Выбрать срок аренды")
    def select_rent_period(self, rent_period_locator):
        self.click_on_element(OrderFormLocators.RENT_PERIOD_FIELD)
        self.scroll_to_element(rent_period_locator)
        self.click_on_element(rent_period_locator)

    @allure.step("Выбрать цвет самоката")
    def select_scooter_colour(self, scooter_colour_locator):
        self.click_on_element(scooter_colour_locator)

    @allure.step("Оставить комментарий для курьера")
    def leave_comment(self, comment):
        self.click_on_element(OrderFormLocators.COMMENT_FOR_COURIER)
        self.send_keys_to_input(OrderFormLocators.COMMENT_FOR_COURIER, comment)

    @allure.step("Нажать на кнопку Заказать")
    def click_on_order_button(self):
        self.click_on_element(OrderFormLocators.ORDER_BUTTON)
        self.wait_for_element(ConfirmationOrderWindowLocators.DO_YOU_WANNA_ORDER_HEADER)

    @allure.step("Нажать на кнопку Да")
    def click_on_yes_button(self):
        self.click_on_element(ConfirmationOrderWindowLocators.YES_BUTTON)
        self.wait_for_element(SuccessfulOrderPageLocators.ORDER_NUMBER_TEXT)



