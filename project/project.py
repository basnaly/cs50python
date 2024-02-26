import csv, sys


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
        self.total = 0


    def __str__(self):
        return f'You selected: {self.name} {self.icon} price: ${self.price}, quantity: {self.quantity}, sum: ${self.sum}'


    @classmethod
    def get_product(cls):
        while True:
            try:
                selected_index = int(input('Your choice: '))
                if selected_index < 0 or selected_index > len(FARM_LIST):
                    continue
                else:
                    type = FARM_LIST[selected_index-1]['type']
                    name = FARM_LIST[selected_index-1]['name']
                    icon = FARM_LIST[selected_index-1]['icon']
                    product_price = FARM_LIST[selected_index-1]['price']
                    price, _ = product_price.split('/')

                return cls(type, name.title(), icon, price)

            except  ValueError as e:
                print(e)
                continue


    def set_quantity_sum(self):
        while True:
            try:
                selected_quantity = float(input('Select quantity, max is 5: '))

                if selected_quantity < 0 or selected_quantity > MAX_QUANTITY:
                    continue
                else:
                    self.quantity = selected_quantity
                    self.sum = round(self.quantity * float(self.price), 2)

                return

            except  ValueError as e:
                continue


    def save_product_to_csv(self, writer):
        row = ({
            'name': self.name,
            'icon': self.icon,
            'price': self.price,
            'quantity': self.quantity,
            'sum': self.sum
        })
        writer.writerow(row)


def main():
    print('Welcome to our online organic farm store!')
    print('You can order our fresh greenery, vegatables and fruit from the list below:')

    print('Pick you option: ')

    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    try:
        csv_file = 'basket.csv'
        with open(csv_file, mode='w', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'icon', 'price', 'quantity', 'sum'])
            writer.writeheader()

            current_product = Product.get_product()
            current_product.set_quantity_sum()
            current_product.save_product_to_csv(writer)

        print(current_product)

        print('Select another product or exit by using Ctrl-D')

    except FileNotFoundError:
        sys.exit('File not found')


if __name__ == '__main__':
    main()
