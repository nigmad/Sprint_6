import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидать URL, содержащий подстроку')
    def wait_for_url_contains(self, substring, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(substring))

    @allure.step('Ожидать появления указанного числа окон')
    def wait_for_number_of_windows(self, number, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(number))

    @allure.step('Найти элемент')
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url