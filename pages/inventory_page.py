from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Localizadores generales
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart_by_name(self, product_name):
        xpath_button = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_button)))

        try:
            button.click()
            WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.XPATH, xpath_button), "Remove"))
        except TimeoutException:
            self.logger.warning(f"Clic normal falló para '{product_name}', reintentando con JS")
            self.driver.execute_script("arguments[0].click();", button)
            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, xpath_button), "Remove"))
        """
        button = self.find_element(By.XPATH, xpath_button)
        button.click()"""

    def get_cart_badge_count(self):
        badge = self.get_text(self.CART_BADGE)
        return badge