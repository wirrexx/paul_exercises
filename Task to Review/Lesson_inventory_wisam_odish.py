from dataclasses import dataclass
import json


@dataclass
class Product:
    name: str
    unit_price: float
    quantity: int
    product_id: int


@dataclass
class Inventory:
    products: list = None

    def __init__(self):
        if self.products is None:
            self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        update_products = [
            product for product in self.products if product_id]
        self.products = update_products

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty")
        else:
            for product in self.products:
                print(
                    f'ID: {product.product_id}\nName: {product.name}\nPrice: {product.unit_price}€\nQuantity: {product.quantity}\n')

    def save_json(self, filename):
        with open(filename, 'w') as file:
            json.dump([product.__dict__ for product in self.products], file)
    
    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.products = [Product(**product_data) for product_data in data]
            
    

# Example usage:
product1 = Product(name='Asus Vivobook', unit_price=2499.99,
                   quantity=25, product_id=1)
product2 = Product(name='Tonyhawk Pro Skater 2',
                   unit_price=69.99, quantity=50, product_id=2)
product3 = Product(name='Die Hard 2',
                   unit_price=4.99, quantity=3, product_id=3)

inventory_new = Inventory()

inventory_new.add_product(product1)
inventory_new.add_product(product2)
inventory_new.add_product(product3)
inventory_new.save_json('inventory.json')
inventory_new.products = []
inventory_new.load_from_json('inventory.json')
# Display the inventory
inventory_new.display_inventory()
