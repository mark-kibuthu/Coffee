from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers and coffee instances
customer1 = Customer("John")
customer2 = Customer("Jane")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create orders
order1 = customer1.create_order(coffee1, 5.0)
order2 = customer2.create_order(coffee2, 4.5)

# Debugging: print out data
print(f"{customer1.name} ordered {coffee1.name} for ${order1.price}")
print(f"{customer2.name} ordered {coffee2.name} for ${order2.price}")

# Test aggregate methods
print(f"Average price of {coffee1.name}: ${coffee1.average_price()}")
print(f"Most aficionado for {coffee1.name}: {Coffee.most_aficionado(coffee1).name}")
