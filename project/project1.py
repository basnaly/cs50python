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

            while True:

                try:
                    selected_index = int(input('Your choice: '))

                    if selected_index < 0 or selected_index > len(FARM_LIST):
                        continue
                    else:
                        product_name = FARM_LIST[selected_index-1]['name']
                        product_icon = FARM_LIST[selected_index-1]['icon']

                    quantity = float(input('Select quantity, max is 5: '))
                    print(quantity)

                    if quantity < 0 or quantity > MAX_QUANTITY:
                        continue
                    else:
                        product_quantity = float(quantity)
                        product_price = FARM_LIST[selected_index-1]['price']
                        price, _ = product_price.split('/')
                        product_sum = round(product_quantity * float(price), 2)

                    save_product_to_csv(product_name, product_icon, product_price, product_quantity, product_sum, writer)

                    print(f'You selected: {product_name}, {product_icon} price: ${product_price}, quantity: {product_quantity}, sum: ${product_sum}')

                    print('Select another product, finish your order or exit Ctrl-D')

                except ValueError as e:
                    print(e)
                    continue

    except FileNotFoundError():
        sys.exit('File not found')



def save_product_to_csv(product_name, product_icon, product_price, product_quantity, product_sum, writer):

    row = ({'name': product_name, 'icon': product_icon, 'price': product_price, 'quantity': product_quantity, 'sum': product_sum})
    writer.writerow(row)



if __name__ == '__main__':
    main()
