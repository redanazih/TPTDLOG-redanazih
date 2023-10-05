class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

# Example of creating an Item object
i = Item(10, 20)

# Accessing price and weight attributes
print("Price:", i.price)
print("Weight:", i.weight)
