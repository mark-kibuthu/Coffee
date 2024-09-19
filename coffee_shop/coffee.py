class Coffee:
    all_coffees = []  

    def __init__(self, name):
        """Initialize a Coffee instance with a name."""
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters.")
        Coffee.all_coffees.append(self)  

    @property
    def name(self):
        """Return the name of the coffee."""
        return self._name

    @classmethod
    def all(cls):
        """Return all coffee instances."""
        return cls.all_coffees

    def orders(self):
        """Return all orders for this coffee."""
        from order import Order  
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        """Return a list of customers who have ordered this coffee."""
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        """Return the number of orders for this coffee."""
        return len(self.orders())

    def average_price(self):
        """Return the average price of orders for this coffee."""
        orders = self.orders()
        total_price = sum(order.price for order in orders)
        return total_price / len(orders) if orders else 0

    @classmethod
    def most_aficionado(cls, coffee):
        """Return the customer who has spent the most on the given coffee."""
        from order import Order  
        customers_spending = {}
        for order in coffee.orders():
            if order.customer not in customers_spending:
                customers_spending[order.customer] = 0
            customers_spending[order.customer] += order.price

        return max(customers_spending, key=customers_spending.get, default=None)
