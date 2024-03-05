from constants import FARM_LIST, MAX_QUANTITY


# Class of Product in cart
class Product:
    def __init__(self, name, icon, price):
        self.name = name
        self.icon = icon
        self.price = price
        self.quantity = 0
        self.sum = 0


    def __str__(self):
        return f'Name: {self.name}, Icon: {self.icon}, Price/Kg: {self.price}, Quantity: {self.quantity}, Sum $: {self.sum}\n'


    @classmethod
    def get_product(cls):
        while True:
            try:
                # Get product's index
                selected_index = int(input('\nSelect product: '))
                if selected_index < 0 or selected_index > len(FARM_LIST):
                    continue
                else:
                    # Get product data according to the selected index
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
                # Get quantity of the produt
                selected_quantity = float(input('Select quantity, kg: '))
                if selected_quantity < 0 or selected_quantity > MAX_QUANTITY:
                    continue
                else:
                    self.quantity = selected_quantity
                    self.calculate_sum()

                return

            except ValueError:
                continue


    def calculate_sum(self):
        # Calculate the sum of the product
        self.sum = round(self.price * float(self.quantity), 2)

    def save_to_csv(self, writer):

        # Save data of product in csv file
        row = self.get_product_obj()
        writer.writerow(row)


    def get_product_obj(self):
        # Get product data as dict
        return {
            'Name': self.name,
            'Icon': self.icon,
            'Price/Kg': self.price,
            'Quantity': self.quantity,
            'Sum $': self.sum
        }
