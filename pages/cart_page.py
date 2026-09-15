from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')

    def go_to_cart(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CART_ICON))
        try:
            element.click()
            self.wait.until(EC.presence_of_element_located(self.CHECKOUT_BUTTON))
        except Exception:
            self.logger.warning("Clic normal en carrito no navegó, reintentando con JS")
            self.driver.execute_script("arguments[0].click();", element)
            self.wait.until(EC.presence_of_element_located(self.CHECKOUT_BUTTON))

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
