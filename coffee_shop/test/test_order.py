import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("Eve")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 4.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

def test_invalid_price():
    customer = Customer("Eve")
    coffee = Coffee("Cappuccino")
    with pytest.raises(ValueError):
        Order(customer, coffee, 12.0)
