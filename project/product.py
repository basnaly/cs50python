
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
        # return f'You selected: {self.name} {self.icon}, price: {self.price}, quantity: {self.quantity}, sum: {self.sum}\n'
        return f'{
            name: {self.name},
            icon: {self.icon},
            price: {self.price},
            quantity: {self.quantity},
            sum: {self.sum}
        }


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

    def set_quantity_sum(self):
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

    def save_to_csv(self, writer):
        row = ({
            'Name': self.name,
            'Icon': self.icon,
            'Price/Kg': self.price,
            'Quantity': self.quantity,
            'Sum $': self.sum
        })
        writer.writerow(row)

