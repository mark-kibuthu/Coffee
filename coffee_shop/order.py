class Order:
    all_orders = []  

    def __init__(self, customer, coffee, price):
        """Initialize an Order instance with a customer, coffee, and price."""
        from customer import Customer  
        from coffee import Coffee  

        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer.")
        
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee.")
        
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        
        Order.all_orders.append(self)  

    @property
    def customer(self):
        """Returns the customer who placed the order."""
        return self._customer

    @property
    def coffee(self):
        """Returns the coffee in the order."""
        return self._coffee

    @property
    def price(self):
        """Returns the price of the order."""
        return self._price

    @classmethod
    def all(cls):
        """Returns all order instances."""
        return cls.all_orders

    @classmethod
    def find_by_customer(cls, customer):
        """Returns all orders placed by a specific customer."""
        from customer import Customer 
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer.")
        return [order for order in cls.all_orders if order.customer == customer]

    @classmethod
    def find_by_coffee(cls, coffee):
        """Returns all orders of a specific coffee."""
        from coffee import Coffee  
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee.")
        return [order for order in cls.all_orders if order.coffee == coffee]
