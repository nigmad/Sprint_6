from selenium.webdriver.common.by import By


class MainPageLocators:


    SAMOKAT_HOME_HEADER = (By.CLASS_NAME, "Home_Header__iJKdX")
    YANDEX_LOGO =(By.XPATH, '//a[@href="//yandex.ru"]')
    SAMOKAT_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    BOTTOM_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, 'button.Button_Button__ra12g')
