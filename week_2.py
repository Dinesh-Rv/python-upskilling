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

