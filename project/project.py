import csv


FARM_LIST = [
    {'type': 'vegatable', 'name': 'carrot', 'icon': '🥕', 'price': '0.70/kg'},
    {'type': 'fruit', 'name': 'banana', 'icon': '🍌', 'price': '1.20/kg'},
    {'type': 'vegatable', 'name': 'cucumber', 'icon': '🥒', 'price': '0.60/kg'},
    {'type': 'fruit', 'name': 'apple', 'icon': '🍎', 'price': '1.30/kg'},
    {'type': 'vegatable', 'name': 'tomato', 'icon': '🍅', 'price': '0.90/kg'},
]

MAX_QUANTITY = 5


def main():
    print('Welcome to our online organic farm store!')
    print('You can order our fresh greenery, vegatables and fruit from the list below:')

    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    while True:


        try:
            selected_index = int(input('Your choice: '))

            if selected_index < 0 or selected_index > len(FARM_LIST):
                continue

            product_name = FARM_LIST[selected_index-1]['name']
            product_icon = FARM_LIST[selected_index-1]['icon']

            quantity = float(input('Select quantity, max is 5: '))

            if quantity < 0 or quantity > MAX_QUANTITY:
                continue

            product_quantity = quantity
            product_price = FARM_LIST[selected_index-1]['price']
            product_sum = round(float(product_quantity) * float(product_price), 2)
            print(product_sum)


            print(f'You selected: {product_name}, {product_icon} price: {product_price}, quantity: {product_quantity}, sum: {product_sum}')

            save_product_to_csv(product_name, product_quantity, product_price, product_sum)
            print('Select another product or exit Ctrl-D')

        except ValueError:
            continue


def save_product_to_csv(product_name, product_icon, product_quantity, product_price, product_sum):
    csv_file = 'basket.csv'
    try:
        with open(csv_file, mode='a', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'icon', 'price', 'quantity', 'sum'])
            writer.writeheader()
            row = ({
                'name': product_name, 'icon': product_icon, 'price': product_price, 'quantity': product_quantity, 'sum': product_sum
            })
            writer.writerow(row)

    except FileNotFoundError():
        sys.exit('File not found')

if __name__ == '__main__':
    main()
