class Product:
    def __init__(self, name, price=None):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{type(self).__name__}(name={self.name!r}, price={self.price})"
    def __repr__(self):
        return str(self)

class Laptop(Product):
    pass

class Smartphone(Product):
    pass

PR1 = Laptop("Asus", 39900)
PR2 = Smartphone("GUD", 700)

print(PR1, PR1.name)
print(PR2)