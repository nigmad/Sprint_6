import pytest
import allure

from data import Data
from pages.questions_page import QuestionsPage



class TestAnswersText:
    @allure.title("Текст ответа на вопрос")
    @pytest.mark.parametrize('question_number, expected_text', Data.answer_to_question)
    def test_answers_text(self, driver, question_number, expected_text):
        questions_page = QuestionsPage(driver)
        questions_page.scroll_to_question_list()
        questions_page.click_on_question(question_number)

        assert questions_page.check_answer_text(question_number, expected_text)