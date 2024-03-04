from termcolor import colored, cprint


FARM_LIST = [
    {'Name': 'Carrot', 'Icon': '🥕', 'Price/Kg': '2.60/kg'},
    {'Name': 'Banana', 'Icon': '🍌', 'Price/Kg': '4.80/kg'},
    {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': '1.20/kg'},
    {'Name': 'Apple', 'Icon': '🍎', 'Price/Kg': '4.30/kg'},
    {'Name': 'Tomato', 'Icon': '🍅', 'Price/Kg': '2.70/kg'},
    {'Name': 'Potato', 'Icon': '🥔', 'Price/Kg': '1.5/kg'},
    {'Name': 'Broccoli', 'Icon': '🥦', 'Price/Kg': '4.7/kg'},
    {'Name': 'Corn', 'Icon': '🌽', 'Price/Kg': '3.5/kg'},
    {'Name': 'Grape', 'Icon': '🍇', 'Price/Kg': '21.3/kg'},
    {'Name': 'Garlic', 'Icon': '🧄', 'Price/Kg': '12.8/kg'},
    {'Name': 'Eggplant', 'Icon': '🍆', 'Price/Kg': '4.6/kg'},
    {'Name': 'Letuce', 'Icon': '🥬', 'Price/Kg': '3.9/kg'},
    {'Name': 'Hot paper', 'Icon': '🌶️', 'Price/Kg': '12.9/kg'},
    {'Name': 'Onion', 'Icon': '🧅', 'Price/Kg': '0.9/kg'},
    {'Name': 'Green Paper', 'Icon': '🫑', 'Price/Kg': '7.5/kg'},
    {'Name': 'Sweet potato', 'Icon': '🍠', 'Price/Kg': '1.9/kg'},
    {'Name': 'Green Pea', 'Icon': '🫛', 'Price/Kg': '8.2/kg'},
    {'Name': 'Melon', 'Icon': '🍈', 'Price/Kg': '14.8/kg'},
    {'Name': 'Watermelon', 'Icon': '🍉', 'Price/Kg': '12.7/kg'},
    {'Name': 'Tangerine', 'Icon': '🍊', 'Price/Kg': '7.2/kg'},
    {'Name': 'Lemon', 'Icon': '🍋', 'Price/Kg': '6.5/kg'},
    {'Name': 'Pineapple', 'Icon': '🍍', 'Price/Kg': '18.3/kg'},
    {'Name': 'Pear', 'Icon': '🍐', 'Price/Kg': '8.7/kg'},
    {'Name': 'Peach', 'Icon': '🍑', 'Price/Kg': '6.5/kg'},
    {'Name': 'Cherries', 'Icon': '🍒', 'Price/Kg': '18.4/kg'},
    {'Name': 'Strawberries', 'Icon': '🍓', 'Price/Kg': '15.8/kg'},
    {'Name': 'Avocado', 'Icon': '🥑', 'Price/Kg': '8.5/kg'},
    {'Name': 'Blieberries', 'Icon': '🫐', 'Price/Kg': '29.0/kg'},
    {'Name': 'Mango', 'Icon': '🥭', 'Price/Kg': '3.9/kg'},
    {'Name': 'Ginger root', 'Icon': '🫚', 'Price/Kg': '19.5/kg'},
]

MAX_QUANTITY = 5


class Product:
    def __init__(self, name, icon, price):
        self.name = name
        self.icon = icon
        self.price = price
        self.quantity = 0
        self.sum = 0


    def __str__(self):
        # return f'You selected: {self.name} {self.icon}, price: {self.price}, quantity: {self.quantity}, sum: {self.sum}\n'
        return f'Name: {self.name}, Icon: {self.icon}, Price/Kg: {self.price}, Quantity: {self.quantity}, Sum $: {self.sum}\n'


    @classmethod
    def get_product(cls):
        while True:
            try:
                selected_index = int(input('Select product: '))
                if selected_index < 0 or selected_index > len(FARM_LIST):
                    continue
                elif selected_index in FARM_LIST[selected_index-1]:
                    cprint('You have already had the product in your order!', 'green')
                    cprint('If you want to edit this product, please run `python project.py -m edit`')
                    continue
                else:
                    name = FARM_LIST[selected_index-1]['Name']
                    icon = FARM_LIST[selected_index-1]['Icon']
                    current_price = FARM_LIST[selected_index-1]['Price/Kg']
                    price, _ = current_price.split('/')

                return cls(name.title(), icon, float(price))

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
        row = self.get_product_obj()
        writer.writerow(row)


    def get_product_obj(self):
        return {
            'Name': self.name,
            'Icon': self.icon,
            'Price/Kg': self.price,
            'Quantity': self.quantity,
            'Sum $': self.sum
        }
