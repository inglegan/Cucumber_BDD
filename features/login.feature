Feature: Autenticación de usuarios en SauceDemo
  Como usuario de la tienda
  Quiero autenticarme con mis credenciales
  Para poder acceder al catálogo de productos

  Background:
    Given el usuario abre la página de inicio de sesión

  Scenario: Inicio de sesión con credenciales válidas
    When el usuario ingresa el usuario "standard_user" y la contraseña "secret_sauce"
    Then el usuario debería ser redirigido a la página de inventario

  Scenario Outline: Validaciones de error en autenticación
    When el usuario ingresa el usuario "<usuario>" y la contraseña "<password>"
    Then debería mostrarse el mensaje de error "<mensaje>"

    Examples:
      | usuario         | password        | mensaje                                                                 |
      | locked_out_user | secret_sauce    | Epic sadface: Sorry, this user has been locked out.                     |
      | standard_user   | wrong_password  | Epic sadface: Username and password do not match any user in this service|
      |                 | secret_sauce    | Epic sadface: Username is required                                      |