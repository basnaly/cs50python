from project import Product


def test_create_product():
    product = Product('Carrot', '🥕', '2.60/kg')
    product.quantity = 2
    product.calculate_sum()

