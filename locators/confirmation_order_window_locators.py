from selenium.webdriver.common.by import By

class ConfirmationOrderWindowLocators:
    DO_YOU_WANNA_ORDER_HEADER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']")
    YES_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']")



