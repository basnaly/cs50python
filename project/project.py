import csv


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
        return f'You selected: {product_name} {product_icon} price: ${product_price}, quantity: {product_quantity}, sum: ${product_sum}'


    @classmethod
    def get_product(cls):
        while True:
            try:
                selected_index = int(input('Your choice: '))
                if selected_index < 0 or selected_index > len(FARM_LIST):
                    continue
                else:
                    self.name = FARM_LIST[selected_index-1]['name']
                    self.icon = FARM_LIST[selected_index-1]['icon']
                    self.price = FARM_LIST[selected_index-1]['price']

                selected_quantity = float(input('Select quantity, max is 5: '))
                print(quantity)

                if selected_quantity < 0 or selected_quantity > MAX_QUANTITY:
                    continue
                else:
                    price, _ = product_price.split('/')
                    self.sum = round(product_quantity * float(price), 2)
            except  ValueError as e:
                print(e)
                continue


    def save_product(self, writer):
        row = ({
            'name': self.name,
            'icon': self.icon,
            'price': self.price,
            'quantity': self.quantity,
            'sum': self.sum})
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

        print('Select another product or exit by using Ctrl-D')

    except FileNotFoundError():
        sys.exit('File not found')


if __name__ == '__main__':
    main()
