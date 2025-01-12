from selenium.webdriver.common.by import By


class OrderFormLocators:
    NAME =(By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME =(By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS =(By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_FIELD =(By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE =(By.XPATH, '//input[contains(@placeholder, "Телефон")]')
    NEXT_BUTTON =(By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Далее"]')

    ABOUT_ORDER_HEADER = (By.CLASS_NAME, "Order_Header__BZXOb")
    WHEN_DELIVER_SCOOTER_FIELD = (By.XPATH, "//input[@type='text' and @placeholder='* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker-popper")
    SCOOTER_COLOUR_FIELD = (By.CSS_SELECTOR, "Order_Checkboxes__3lWSI")
    SCOOTER_COLOUR_BLACK = (By.ID, "black")
    SCOOTER_COLOUR_GREY = (By.ID, "grey")
    COMMENT_FOR_COURIER = (By.XPATH, "//input[@type='text' and @placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")


    METRO_STATION_USER_1 = (By.XPATH, "//div[contains(text(),'Бульвар Рокоссовского')]")
    METRO_STATION_USER_2 = (By.XPATH, "//div[contains(text(), 'Преображенская площадь')]")
    RENT_PERIOD_USER_1 = (By.XPATH, "//div[contains(text(), 'двое суток')]")
    RENT_PERIOD_USER_2 = (By.XPATH, "//div[contains(text(), 'трое суток')]")
    ORDER_DATE_USER_1 = (By.XPATH, "//div[@aria-label='Choose воскресенье, 12-е января 2025 г.']")
    ORDER_DATE_USER_2 = (By.XPATH, "//div[@aria-label='Choose пятница, 17-е января 2025 г.']")