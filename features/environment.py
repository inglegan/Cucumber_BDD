import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def before_scenario(context, scenario):
    options = Options()
    # Si corre en CI, se activa el modo headless automáticamente
    if os.getenv("CI", "false").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    # Si el escenario falla, adjunta captura de pantalla a Allure
    if scenario.status == "failed":
        screenshot = context.driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=f"Fallo_{scenario.name}",
            attachment_type=allure.attachment_type.PNG
        )
    if hasattr(context, "driver"):
        context.driver.quit()