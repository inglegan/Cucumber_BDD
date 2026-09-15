from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
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

@when('el usuario va al carrito de compras y hace clic en Checkout')
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.go_to_cart()
    context.cart_page.click_checkout()

@when('el usuario ingresa sus datos de envío con Nombre "{first_name}", Apellidos "{last_name}" y Código Postal "{postal_code}"')
def step_impl(context, first_name, last_name, postal_code):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_checkout_information(first_name, last_name, postal_code)
    context.checkout_page.click_continue()

@when('el usuario finaliza la compra')
def step_impl(context):
    context.checkout_page.click_finish()

@then('el mensaje de confirmación de compra debe ser "{expected_message}"')
def step_impl(context, expected_message):
    message = context.checkout_page.get_confirmation_message()
    assertpy.assert_that(message).is_equal_to(expected_message)