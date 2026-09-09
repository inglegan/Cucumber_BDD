import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s]: %(message)s")

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logging.getLogger(self.__class__.__name__)

    def open_url(self, url: str):
        self.logger.info(f"Navegando a: {url}")
        self.driver.get(url)

    def click(self, locator: tuple):
        self.logger.info(f"Haciendo clic en: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: tuple, text: str):
        self.logger.info(f"Ingresando texto en: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator: tuple) -> bool:
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()