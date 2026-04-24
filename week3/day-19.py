import re

email = "dinesh@gmail.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0.9.-]+\.[a-zA-Z]{2,}$]"
if re.match(pattern, email):
    print("Valid email!")


phone = "9876543210"
pattern = r"^[6-9]\d{9}$"
if re.match(pattern, phone):
    print("Valid Phone!")


pincode = "641001"
pattern = r"^\d{6}$"
if re.match(pattern, pincode):
    print("Valid Pincode!")

password = "Dinesh@123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\d)(?=.*[@#$%].{8,}$)"
if re.match(pattern, password):
    print("Strong Password!")

text = "Order #1234 - 2 Burgers at Rs.150 each, total Rs.300"
numbers = re.findall(r"\d", text)
print(numbers)