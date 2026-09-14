from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def click_continue(self):
        self.find_element(*self.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.find_element(*self.FINISH_BUTTON).click()

    def get_confirmation_message(self):
        return self.find_element(*self.SUCCESS_MESSAGE).text