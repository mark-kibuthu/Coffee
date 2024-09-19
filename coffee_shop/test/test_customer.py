import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initialization():
    customer = Customer("John")
    assert customer.name == "John"

def test_customer_invalid_name():
    with pytest.raises(ValueError):
        Customer("")

def test_customer_create_order():
    customer = Customer("Jane")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
