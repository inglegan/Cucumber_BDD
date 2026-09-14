from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
import assertpy

@given('el usuario inicia sesión con las credenciales válidas "{username}" y "{password}"')
def step_impl(context, username, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_url("https://www.saucedemo.com/")
    context.login_page.perform_login(username, password)
    context.inventory_page = InventoryPage(context.driver)

@when('el usuario agrega los siguientes productos al carrito:')
def step_impl(context):
    for row in context.table:
        product_name = row['producto']
        context.inventory_page.add_product_to_cart_by_name(product_name)

@then('el carrito de compras debería mostrar {count:d} productos seleccionados')
def step_impl(context, count):
    cart_count = context.inventory_page.get_cart_badge_count()
    assertpy.assert_that(int(cart_count)).is_equal_to(count)