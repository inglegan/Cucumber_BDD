from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ICON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def go_to_cart(self):
        self.find_element(*self.CART_ICON).click()

    def click_checkout(self):
        self.find_element(*self.CHECKOUT_BUTTON).click()