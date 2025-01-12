from selenium.webdriver.common.by import By

class SuccessfulOrderPageLocators:
    ORDER_NUMBER_TEXT = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']//div[@class='Order_Text__2broi' and contains(text(), 'Номер заказа:')]")
    LOOKUP_ORDER_STATUS_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g', 'Button_Middle__1CSJM' and text()='Посмотреть статус']")


