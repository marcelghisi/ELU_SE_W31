import unittest
from shopping_cart import CalculateTotal

class TestShoppingCart(unittest.TestCase):
    def test_calculate_total(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        result = CalculateTotal(cart)
        self.assertEqual(result, 25.47)

if __name__ == '__main__':
    unittest.main()

