from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Localizadores generales
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart_by_name(self, product_name):
        # En SauceDemo, el botón dinámico se puede encontrar localizando el texto del producto
        # y encontrando el botón 'Add to cart' asociado dentro de su contenedor.
        xpath_button = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_button)))
        button.click()
        """
        button = self.find_element(By.XPATH, xpath_button)
        button.click()"""

    def get_cart_badge_count(self):
        badge = self.find_element(*self.CART_BADGE)
        return badge.text
