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

# --- Day 10 ---

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} | Area: {self.area():.2f}"

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__ (self, other):
        return self.area() == other.area()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


c = Circle(5)
r = Rectangle(4, 6)

print(c)
print(r)
print(c > r)
print(c == r)

shapes = [Circle(3), Rectangle(10, 2), Circle(7)]

for shape in sorted(shapes):
    print(shape)

# Excercise

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bonus(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

class FullTimeEmployee(Employee):
    # bonus = 20
    # role = "Full Time"

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.20

    def get_role(self):
        return "Full Time"

    def __str__(self):
        bonus_rate = self.calculate_bonus()
        return f"Name: {self.name} | Role: {self.get_role()} | Bonus: {bonus_rate}"

    
class ContractEmployee(Employee):
    # bonus = 10
    # role = "Contract"

    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def get_role(self):
        return "Contract"  

    def calculate_bonus(self):
        return (self.hourly_rate * self.hours) * 0.10

    def __str__(self):
        bonus_rate = self.calculate_bonus()
        return f"Name: {self.name} | Role: {self.get_role()} | Bonus: {bonus_rate}"

from functools import reduce
class ShoppingCart():
    def __init__(self):
        self.cart = []

    def add(self, item, price):
        self.cart.append((item, price))

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        # return f"All Items: item - {self.item} price - {self.price}"
        items_wrap = "\n".join([f"{item}: Rs.{price}" for item, price in self.cart])
        return f"Cart Items:\n{items_wrap}\n Total: Rs.{self.get_total()}"

    def __add__(self, other):
        new_cart = ShoppingCart()
        # return cart + others
        new_cart.cart = self.cart + other.cart
        return new_cart

    def get_total(self):
        # return reduce(lambda x, y: x.price + y.price, self.cart)
        return sum(price for item, price in self.cart)


employees = [ FullTimeEmployee("Dinesh", 50000), ContractEmployee("Kumar", 5000, 8)]

for emp in employees:
    print(f"Calculated Bonus is: {emp.calculate_bonus()}")

for emp in employees:
    print(emp)

cart1 = ShoppingCart()
cart1.add("Laptop", 75000)
cart1.add("Mouse", 1500)

cart2 = ShoppingCart()
cart2.add("Keyboard", 2500)
cart2.add("Monitor", 15000)

print(f"Cart 1 items: {len(cart1)}")
print(cart1)

combined = cart1 + cart2
print(f"Combined items: {len(combined)}")
print(combined)


