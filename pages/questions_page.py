import allure
from pages.base_page import BasePage
from locators.questions_page_locatos import QuestionsPageLocators

class QuestionsPage(BasePage):



    @allure.step('Скролл до списка вопросов')
    def scroll_to_question_list(self):
        self.scroll_to_element(QuestionsPageLocators.QUESTIONS)

    @allure.step('Открыть ответ на вопрос')
    def click_on_question(self, question_number):
        question_locator = QuestionsPageLocators.question_number(question_number)
        answer_locator = QuestionsPageLocators.answer_number(question_number)
        self.scroll_to_element(question_locator)
        self.wait_for_element(question_locator, 20)
        self.click_on_element(question_locator)
        self.wait_for_element(answer_locator, 20)

    @allure.step('Сравнить текст ответа на вопрос')
    def check_answer_text(self, question_number, expected_text):
        answer_locator = QuestionsPageLocators.answer_number(question_number)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text



