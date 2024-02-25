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

    while True:
        print('Pick you option: ')

        try:

            for index, item in enumerate(FARM_LIST):
                print(f'{index+1}) {item["name"]} {item["price"]}')

            selected_number = int(input('Your choice: '))

            if selected_number < 0 or selected_number > len(FARM_LIST):
                continue

            product_name = FARM_LIST[selected_number]['name']

            selected_quantity = float(input('Select quantity, until 5 kg: '))

            if selected_quantity < 0 or selected_quantity > 5:
                continue

            product_quantity = selected_quantity
            product_price = FARM_LIST[selected_number]['price']
            product_sum = round(product_quantity * product_price, 2)

            save_product_to_csv(product_name, product_quantity, product_price, product_sum)

        except ValueError:
            continue


def save_product_to_csv(product_name, product_quantity, product_price, product_sum):
    csv_file_path = 'basket.csv'
    with open(csv_file_path, mode='a', newline='\n') as file:
        writer = csv.DictWriter()


if __name__ == '__main__':
    main()
