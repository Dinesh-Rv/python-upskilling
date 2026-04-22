def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print("After... calling")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b


print(add(10, 5))


#####

from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper


def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@bold
@uppercase
def greet(name):
    """This Function Greets by the name"""
    return f"Hello {name}"

print(greet("Dinesh"))
print(greet.__name__)
print(greet.__doc__)


# --- Exercise ---
# Decorators

from functools import wraps
# import datetime
from datetime import datetime

def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # even_numbers = filter( 
        #     lambda number:
        #         if number % 2 != 0:
        #             print("Invalid input")
        #             break
        #         else:
        #             return number           
        # )    
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print(f"Invalid Input! {arg} is not a positive Number!")
                return None
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"{func.__name__} started at {start_time}")
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"{func.__name__} ended at {end_time}")
        diff = end_time - start_time
        print(f"Time took to run function {diff}")
        return result
    return wrapper

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function Name : {func.__name__}")
        # print(f"Arguments Passed : {func.__args__}")
        print(f"Arguments Passed : {args}")
        result = func(*args, **kwargs)
        print(f"Result is: {result}")
        return result
    return wrapper


@validate_input
@timer
@log_activity
def calculate_discount(price, discount_percentage):
    discount_amount= price*discount_percentage/100
    discount_price= price - discount_amount
    return discount_price

print("====Valid Input====")
calculate_discount(1000, 10)

print("\n====Invalid Input====")
calculate_discount(-500, 10)