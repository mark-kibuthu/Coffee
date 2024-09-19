class Customer:
    all_customers = []  

    def __init__(self, name):
        
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        
       
        Customer.all_customers.append(self)

    @property
    def name(self):
        """Returns the customer's name."""
        return self._name

    @classmethod
    def all(cls):
        """Returns all customer instances."""
        return cls.all_customers

    def orders(self):
        """Returns all orders associated with this customer."""
        from order import Order  
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        """Returns a list of unique coffees ordered by this customer."""
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        """Creates a new order for this customer."""
        from order import Order  
        return Order(self, coffee, price)
