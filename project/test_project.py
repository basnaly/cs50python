import argparse
from product import Product
from edit import delete, change_quantity
import pytest


def test_is_create():



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


def test_delete():
    table = [
        {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': 1.20, 'Quantity': 2, 'Sum $': 2.4},
        {'Name': 'Tomato', 'Icon': '🍅', 'Price/Kg': 2.70, 'Quantity': 1.5, 'Sum $': 4.05}
    ]
    delete(table, 1)

    assert table == [
        {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': 1.20, 'Quantity': 2, 'Sum $': 2.4}
    ]


def test_change_quantity():
    table = [
        {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': 1.20, 'Quantity': 2, 'Sum $': 2.4},
        {'Name': 'Tomato', 'Icon': '🍅', 'Price/Kg': 2.70, 'Quantity': 1.5, 'Sum $': 4.05}
    ]
    change_quantity(table, 0, 0.5)

    assert table == [
        {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': 1.20, 'Quantity': 0.5, 'Sum $': 0.6},
        {'Name': 'Tomato', 'Icon': '🍅', 'Price/Kg': 2.70, 'Quantity': 1.5, 'Sum $': 4.05}
    ]


def test_change_quantity_error_index():
    table = [
        {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': 1.20, 'Quantity': 2, 'Sum $': 2.4},
        {'Name': 'Tomato', 'Icon': '🍅', 'Price/Kg': 2.70, 'Quantity': 1.5, 'Sum $': 4.05}
    ]
    with pytest.raises(ValueError):
        change_quantity(table, -1, 0.5)


def test_change_quantity_error_quantity():
    table = [
        {'Name': 'Cucumber', 'Icon': '🥒', 'Price/Kg': 1.20, 'Quantity': 2, 'Sum $': 2.4},
        {'Name': 'Tomato', 'Icon': '🍅', 'Price/Kg': 2.70, 'Quantity': 1.5, 'Sum $': 4.05}
    ]
    with pytest.raises(ValueError):
        change_quantity(table, 0, 6)

