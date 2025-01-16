from selenium.webdriver.common.by import By

class QuestionsPageLocators:
    QUESTIONS = (By.CLASS_NAME, 'accordion__heading')

    @staticmethod
    def question_number(question):
        return By.XPATH, f'//div[@id="accordion__heading-{question}"]'

    @staticmethod
    def answer_number(answer):
        return By.XPATH, f'//div[@id="accordion__panel-{answer}" and @aria-labelledby="accordion__heading-{answer}"]'