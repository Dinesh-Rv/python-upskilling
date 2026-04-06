# --- Day 8 ---

from collections import Counter, defaultdict, namedtuple, deque

words = ["python", "java", "python", "react", "java", "python", "node", "react", "java"]

# Sorry I was blank and had to look the prev code.
word_counts = Counter(words)

print(word_counts)
print(word_counts.most_common(3))

employees = [
       ("Dinesh", "IT"),
       ("Kumar", "IT"),
       ("Raj", "HR"),
       ("Priya", "HR"),
       ("Sneha", "Finance")
]

# empl_grp = defaultdict(tuple)
empl_grp = defaultdict(list)

for empl in employees:
    # empl_grp.append(empl)
    empl_grp[empl[1]].append(empl[0])

print(dict(empl_grp))

# Product = namedtuple([name, price, category])
Product = namedtuple("Product", ["name", "price", "category"])

logi = Product(name = "Mouse", price = 29.99, category = "Electronics")
apsara = Product(name = "Pencil", price = 1.99, category = "Stationary")
portronic = Product(name = "Keyboard", price = 39.99, category = "Electronics")

# print(Product)
print(logi.name, logi.price, logi.category)
print(apsara)
print(portronic)

# print(item) for item in Product:
#     pass

for item in (logi, apsara, portronic):
    print(f"Name: {item.name}, Price: {item.price}, Category: {item.category}")

dq_last_3 = deque(maxlen = 3)

dq_last_3.append("www.firstpage.com")
dq_last_3.append("www.2ndpage.com")
dq_last_3.append("www.thi3dWeb.to")

print(dq_last_3)

dq_last_3.append("www.fou4thie.in")
dq_last_3.append("www.5ivetheweb.la")

print(dq_last_3)


# def even_numbers(n = 0):
#     yield n
#     n += 2

def even_numbers(n = 0):
    while True:
        yield n
        n += 2

get_even = even_numbers()
for _ in range(10):
    print(next(get_even))


# --- Day 9 ---

class Product:
    discount_rate = 0.10

    def __init__(self, name, price, category):
        self.name = name
        self.category = category
        self.__price = price

    def get_price(self):
        return self.__price

    def apply_discount(self):
        discounted = self.__price * ( 1 - Product.discount_rate)
        return round(discounted, 2)

    def get_details(self):
        return f"{self.name} | {self.category} | Rs.{self.__price}"

class ElectronicsProduct(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price, "Electronics")
        self.warranty_years = warranty_years

    def get_details(self):
        base = super().get_details()
        return f"{base} | Warranty: {self.warranty_years} years"


laptop = ElectronicsProduct("Laptop", 75000, 2)
print(laptop.get_details())
print(laptop.apply_discount())
print(laptop.get_price())


# Excercise

class Vehicle:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

        # def accelerate(amount):
        #     speed += amount
        #     return f"Speed Has Increased to {speed}"

        # def brake(amount):
        #     if self.speed > 0:
        #         speed -= amount
        #         return f"Speed Has Descreased to {speed}"
        #     else:
        #         return "Speed is already minimal"

        # def get_info():
        #     return f"Brand: {self.brand} | Model: {self.model} | Speed: {self.speed}"

    def accelerate(self, amount):
        self.speed += amount
        return f"Speed Has Increased to {self.speed}"

    def brake(self, amount):
        # if self.speed > 0:
        #     speed -= amount
        #     return f"Speed Has Descreased to {speed}"
        # else:
        #     return "Speed is already minimal"
        self.speed = max(0, self.speed - amount)
        return f"Speed Has Descreased to {self.speed}"

    def get_info(self):
        return f"Brand: {self.brand} | Model: {self.model} | Speed: {self.speed}"

class ElectricVehicle(Vehicle):
    # def __init__(self, battery_level):
    def __init__(self, brand, model, speed, battery_level):
        # self.battery_level = battery_level
        # super().__init__(self, Vehicle.brand, Vehicle.model, Vehicle.speed)
        super().__init__(brand, model, speed)
        self.battery_level = battery_level

    def charge(self, amount):
        if amount < 0:
            return "Invalid Charge Value"

        if self.battery_level >= 100:
            return "Battery Already at Full power"
        # elif self.battery_level < 100:
        #     self.battery_level += amount
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery charged to {self.battery_level}"

    def get_info(self):
        base = super().get_info()
        return f" {base} | Battery Level: {self.battery_level}%"    



class BankAccount:
    # def __init__(self, __balance, __pin):
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        self.__balance += amount
        return f"Amount Deposited, current Balance is: {self.__balance}"

    def withdraw(self, amount, pin):
        # if(pin == self.__pin):
        if pin == self.__pin:
            self.__balance -= amount
            return f"Amount has been debited by {amount}, current balance: {self.__balance}"
        return "WRONG PIN - Check your pin"

    def get_balance(self):
        return f"Current Balance: {self.__balance}"

# Vehicle objects
dinesh_mhb = Vehicle("Mahindra", "BE6", 0)
kumar_bmw = Vehicle("BMW", "IX1", 0)

print(dinesh_mhb.get_info())
print(dinesh_mhb.accelerate(50))
print(dinesh_mhb.brake(20))
print(dinesh_mhb.get_info())

print(kumar_bmw.get_info())
print(kumar_bmw.accelerate(80))
print(kumar_bmw.brake(30))
print(kumar_bmw.get_info())

# ElectricVehicle objects
tesla = ElectricVehicle("Tesla", "Model 3", 0, 50)
rivian = ElectricVehicle("Rivian", "R1T", 0, 30)

print(tesla.get_info())
print(tesla.accelerate(60))
print(tesla.charge(30))
print(tesla.get_info())

print(rivian.get_info())
print(rivian.accelerate(40))
print(rivian.charge(80))          
print(rivian.get_info())

# BankAccount
account = BankAccount(10000, "5432")
print(account.get_balance())
print(account.deposit(5000))
print(account.withdraw(3000, "5432"))
print(account.withdraw(1000, "9999"))   
print(account.get_balance())