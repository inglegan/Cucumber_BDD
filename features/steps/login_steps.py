from behave import given, when, then, use_step_matcher
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# Activa el motor de expresiones regulares para todo el archivo
use_step_matcher("re")

@given(r'el usuario abre la página de inicio de sesión')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()

@when(r'el usuario ingresa el usuario "(?P<user>.*)" y la contraseña "(?P<password>.*)"')
def step_impl(context, user, password):
    context.login_page.perform_login(user, password)

@then(r'el usuario debería ser redirigido a la página de inventario')
def step_impl(context):
    assert "/inventory.html" in context.driver.current_url, "No se redirigió al catálogo"
    app_logo = context.driver.find_element(By.CLASS_NAME, "app_logo")
    assert app_logo.is_displayed(), "El logo de la tienda no es visible"

@then(r'debería mostrarse el mensaje de error "(?P<mensaje>.*)"')
def step_impl(context, mensaje):
    actual_error = context.login_page.get_error_message()
    assert mensaje in actual_error, f"Esperado: {mensaje} | Obtenido: {actual_error}"

    # Genera reporte de Allure después de la ejecución de los pasos
    # allure generate reports\allure-results -o reports\allure-report --clean
    # genera un server local y abre el reporte en el navegador
    # allure open reports\allure-report
