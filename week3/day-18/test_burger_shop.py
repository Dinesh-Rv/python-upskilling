
import unittest
from custom_exception import ItemNotFoundError

from burger_shop import BurgerShop

# class TestBurgerOrder(unittest.TestCase):
#     bursh_1 = BurgerShop("sam", {
#     "classic": 180,
#     "Premium": 200,
#     "Loaded": 250,
#     "Fries": 100,
#     })

class TestBurgerOrder(unittest.TestCase):

    def setUp(self):
        self.shop = BurgerShop("Test Shop", {
            "Classic": 180,
            "Premium": 200,
            "Loaded": 250,
            "Fries": 100
        })

    def test_add_valid_item(self):
        self.shop.add_to_cart("Classic", 2)
        self.assertEqual(len(self.shop.cart), 2)

    def test_add_invalid_item(self):
        with self.assertRaises(ItemNotFoundError):
            self.shop.add_to_cart("Pizza", 1)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.shop.add_to_cart("Classic", 0)

        with self.assertRaises(ValueError):
            self.shop.add_to_cart("Classic", -1)

    def test_get_total(self):
        self.shop.add_to_cart("Classic", 2)
        self.shop.add_to_cart("Fries", 1)
        self.assertEqual(self.shop.get_total(), 460)

    def test_apply_discount(self):
        self.shop.add_to_cart("Classic", 1)
        result = self.shop.apply_discount(10)
        self.assertEqual(result, 162.0)

    def test_invalid_discount_over_100(self):
        with self.assertRaises(ValueError):
            self.shop.apply_discount(110)

    def test_invalid_discount_negative(self):
        with self.assertRaises(ValueError):
            self.shop.apply_discount(-10)

    def test_empty_cart_total(self):
        self.assertEqual(self.shop.get_total(), 0)


if __name__ == "__main__":
    unittest.main()