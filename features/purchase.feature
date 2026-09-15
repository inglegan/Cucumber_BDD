Feature: Selección de productos y adición al carrito en SauceDemo
  Como usuario autenticado en la tienda
  Quiero seleccionar productos específicos
  Para agregarlos al carrito de compras y completar la orden

  Scenario: Agregar dos productos específicos al carrito de compras y realizar el checkout
    Given el usuario inicia sesión con las credenciales válidas "standard_user" y "secret_sauce"
    When el usuario agrega los siguientes productos al carrito:
      | producto                              |
      | Test.allTheThings() T-Shirt (Red)     |
      | Sauce Labs Bolt T-Shirt               |
      | Sauce Labs Bike Light                 |
      | Sauce Labs Onesie                     |
    Then el carrito de compras debería mostrar 4 productos seleccionados
    When el usuario va al carrito de compras y hace clic en Checkout
    And el usuario ingresa sus datos de envío con Nombre "Miguel Angel", Apellidos "Cuervo de la cruz" y Código Postal "55087"
    And el usuario finaliza la compra
    Then el mensaje de confirmación de compra debe ser "Thank you for your order!"