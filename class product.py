class Product:
    def __init__(self, name, price, quantity):
        self.name = name

        # Validate price
        if price > 0:
            self.price = price
        else:
            self.price = 0.01

        # Validate quantity
        if quantity >= 0:
            self.quantity = quantity
        else:
            self.quantity = 0

    def get_total_value(self):
        return self.price * self.quantity


# Usage
p1 = Product("Laptop", 999, 5)
p2 = Product("Broken", -50, -3)  # bad values fixed

print(p1.get_total_value())  # 4995
print(p2.get_total_value())  # 0.0