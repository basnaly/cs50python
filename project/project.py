import csv, sys
from tabulate import tabulate


FARM_LIST = [
    {'type': 'vegatable', 'name': 'carrot', 'icon': '🥕', 'price': '0.70/kg'},
    {'type': 'fruit', 'name': 'banana', 'icon': '🍌', 'price': '1.20/kg'},
    {'type': 'vegatable', 'name': 'cucumber', 'icon': '🥒', 'price': '0.60/kg'},
    {'type': 'fruit', 'name': 'apple', 'icon': '🍎', 'price': '1.30/kg'},
    {'type': 'vegatable', 'name': 'tomato', 'icon': '🍅', 'price': '0.90/kg'},
]

MAX_QUANTITY = 5


class Product:
    def __init__(self, type, name, icon, price):
        self.type = type
        self.name = name
        self.icon = icon
        self.price = price
        self.quantity = 0
        self.sum = 0


    def __str__(self):
        table = [{'Name': self.name, 'Icon': self.icon, 'Price': self.price, 'Quantity': self.quantity, 'Sum': self.sum}]
        # return f'You selected: {self.name} {self.icon}, price: {self.price}, quantity: {self.quantity}, sum: {self.sum}'
        return tabulate(table, headers='keys', tablefmt='grid')

    @classmethod
    def get_product(cls):

        while True:
            try:
                selected_index = int(input('Select product: '))
                if selected_index < 0 or selected_index > len(FARM_LIST):
                    continue
                else:
                    type = FARM_LIST[selected_index-1]['type']
                    name = FARM_LIST[selected_index-1]['name']
                    icon = FARM_LIST[selected_index-1]['icon']
                    current_price = FARM_LIST[selected_index-1]['price']
                    price, _ = current_price.split('/')

                return cls(type, name.title(), icon, float(price))

            except ValueError:
                continue

    def get_quantity(self):

        while True:
            try:
                selected_quantity = float(input('Select quantity: '))
                if selected_quantity < 0 or selected_quantity > MAX_QUANTITY:
                    continue
                else:
                    self.quantity = selected_quantity
                    self.sum = round(self.price * float(self.quantity), 2)

                return

            except ValueError:
                continue

    def save_product(self):
         with open('basket.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price $', 'Quantity', 'Sum $'])
            writer.writerow({'Name': self.name, 'Icon': self.icon, 'Price $': self.price, 'Quantity': self.quantity, 'Sum $': self.sum})

def main():

    print('Welcome to our online organic farm store!')
    print('Order our fresh greenery, vegatables and fruit from the list below:')

    with open('basket.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price $', 'Quantity', 'Sum $'])
            writer.writeheader()

    while True:
        try:
            print('Pick you option: ')
            for index, product in enumerate(FARM_LIST, start=1):
                print(f'{index}) {product["name"]} {product["icon"]} {product["price"]}')

            current_product = Product.get_product()
            current_product.get_quantity()
            current_product.save_product()

            print(current_product)
            print('Select another one or exit using Ctrl-D')

        except ValueError:
            continue


if __name__ == '__main__':
    main()
