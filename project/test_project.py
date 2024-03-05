from product import Product


def test_create_product():
    product = Product('Carrot', '🥕', 2.6)
    product.quantity = 2
    product.calculate_sum()

    assert product.sum == 5.2
