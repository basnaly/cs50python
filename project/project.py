

FARM_LIST = [
    {'type': 'vegatable', 'name': 'carrot', 'icon': '🥕', 'price': '0.70/kg'},
    {'type': 'fruit', 'name': 'banana', 'icon': '🍌', 'price': '1.20/kg'},
    {'type': 'vegatable', 'name': 'cucumber', 'icon': '🥒', 'price': '0.60/kg'},
    {'type': 'fruit', 'name': 'apple', 'icon': '🍎', 'price': '1.30/kg'},
    {'type': 'vegatable', 'name': 'tomato', 'icon': '🍅', 'price': '0.90/kg'},
]


def main():
    print('Welcome to our online organic farm store!')
    print('You can order our fresh greenery, vegatables and fruit from the list below:')

    while True:
        print('Pick you option: ')
        for index, item in enumerate(FARM_LIST):
            print(f'{index+1}) {item["name"]} {item["price"]}\n')

        print('Your choice: ')

if __name__ == '__main__':
    main()
