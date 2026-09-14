Feature: Selección de productos y adición al carrito en SauceDemo
  Como usuario autenticado en la tienda
  Quiero seleccionar productos específicos
  Para agregarlos al carrito de compras

  Scenario: Agregar cuatro productos específicos al carrito de compras
    Given el usuario inicia sesión con las credenciales válidas "standard_user" y "secret_sauce"
    When el usuario agrega los siguientes productos al carrito:
      | producto                              |
      | Test.allTheThings() T-Shirt (Red)     |
      | Sauce Labs Bolt T-Shirt               |
      | Sauce Labs Bike Light                 |
      | Sauce Labs Onesie                     |
    Then el carrito de compras debería mostrar 4 productos seleccionados