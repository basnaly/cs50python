

FARM_LIST = [
    {'type': 'vegatable', 'name': 'carrot', 'price': '0.70/kg'},
    {'type': 'greenery', 'name': 'parsel', 'price': '0.20/piece'},
    {'type': 'fruit', 'name': 'apple', 'price': '1.30/kg'},
]


def main():
    print('Welcome to our online organic farm store!')
    print('You can order our fresh greenery, vegatables and fruit from the list below:')

    input_message = 'Pick an option:\n'
    for index, item in enumerate(FARM_LIST):
        input_message += f'{index+1}) {item["name"]} {item["price"]}\n'



if __name__ == '__main__':
    main()
