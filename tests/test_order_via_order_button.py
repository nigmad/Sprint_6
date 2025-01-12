import pytest
import allure

from locators.succesfull_order_page_locators import SuccessfulOrderPageLocators
from data import Data
from locators.order_form_locators import OrderFormLocators


class TestOrderViaBottomButton:
    @allure.title("Заказ через нижнюю кнопку Заказать")
    def test_order_via_top_button(self, driver, open_order_site_bottom_button):

        order_page = open_order_site_bottom_button

        order_page.fill_user_data_order_form(Data.name_user_2, Data.surname_user_2, Data.address_user_2, Data.phone_user_2)
        order_page.select_metro_station(OrderFormLocators.METRO_STATION_USER_2)
        order_page.click_next_button()
        order_page.select_order_date(OrderFormLocators.ORDER_DATE_USER_2)
        order_page.select_rent_period(OrderFormLocators.RENT_PERIOD_USER_2)
        order_page.select_scooter_colour(OrderFormLocators.SCOOTER_COLOUR_GREY)
        order_page.leave_comment(Data.comment_user_2)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()

        assert driver.find_element(*SuccessfulOrderPageLocators.ORDER_NUMBER_TEXT)



    class TestOrderViaTopButton:
        @allure.title("Заказ через верхнюю кнопку Заказать")
        def test_order_via_top_button(self, driver, open_order_site_top_button):
            order_page = open_order_site_top_button

            order_page.fill_user_data_order_form(Data.name_user_1, Data.surname_user_1, Data.address_user_1, Data.phone_user_1)
            order_page.select_metro_station(OrderFormLocators.METRO_STATION_USER_1)
            order_page.click_next_button()
            order_page.select_order_date(OrderFormLocators.ORDER_DATE_USER_1)
            order_page.select_rent_period(OrderFormLocators.RENT_PERIOD_USER_1)
            order_page.select_scooter_colour(OrderFormLocators.SCOOTER_COLOUR_BLACK)
            order_page.leave_comment(Data.comment_user_1)
            order_page.click_on_order_button()
            order_page.click_on_yes_button()

            assert driver.find_element(*SuccessfulOrderPageLocators.ORDER_NUMBER_TEXT)







