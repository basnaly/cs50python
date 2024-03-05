from product import Product


def test_product_calculate_sum():
    product = Product('Carrot', '🥕', 2.6)
    product.quantity = 2
    product.calculate_sum()

    assert product.sum == 5.2


def test_get_product_obj():
    product = Product('Apple', '🍎', 4.3)
    product.quantity = 1.5
    product.sum = 6.45
    product_obj = product.get_product_obj()

    assert product_obj == {
        'Name': 'Apple',
        'Icon': '🍎',
        'Price/Kg': 4.3,
        'Quantity': 1.5,
        'Sum $': 6.45
    }


def test_add():
    table = []
    product = Product('Cucumber', '🥒', 1.2)
    product.quantity = 2
    product.sum = 2.4
    table.append(product.get_product_obj())

    assert table == [
        {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': '1.20/kg'}
    ]
