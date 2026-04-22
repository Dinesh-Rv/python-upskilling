from custom_exception import ItemNotFoundError

# menu = {
#     "classic": "180",
#     "Premium": "200",
#     "Loaded": "250",
#     "Fries": "100",
# }

# cart = []

class BurgerShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.cart = []

    def add_to_cart(self, item, quantity):
        try:
            # if item is None or item is "":
            if item not in self.menu:
                raise ItemNotFoundError(f"{item} Not Found!")
            if quantity <= 0:
                raise ValueError("Qty must ne positive")

            for _ in range(quantity):
                self.cart.append(self.menu[item])

            # return sum(self.cart)
        except ItemNotFoundError as e:
            print(e)
            raise

        except ValueError as e:
            print(e)
            raise

        except Exception:
            print("An Error Occurred")
            raise

    def get_total(self):
        return sum(self.cart)

    def apply_discount(self, percent):
        if percent > 100 or percent < 0:
            raise ValueError("Invalid Percentage")
        total_amount = self.get_total()

        # discount_total = total_amount - total_amount * percent/100

        return total_amount - (total_amount * percent / 100)





    


