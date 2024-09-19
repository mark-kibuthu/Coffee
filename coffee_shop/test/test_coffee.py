import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_invalid_name():
    with pytest.raises(ValueError):
        Coffee("")

def test_num_orders():
    coffee = Coffee("Mocha")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    order1 = customer1.create_order(coffee, 4.0)
    order2 = customer2.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Americano")
    customer1 = Customer("Charlie")
    customer2 = Customer("Daisy")
    order1 = customer1.create_order(coffee, 3.0)
    order2 = customer2.create_order(coffee, 7.0)
    assert coffee.average_price() == 5.0
