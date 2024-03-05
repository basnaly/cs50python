from project import main


def test_create_product():
    product = Product('Carrot', '🥕', '2.60/kg')
    product.quantity = 2
    product.sum = 5.2

    assert main([h] [-m MODE]) == True
