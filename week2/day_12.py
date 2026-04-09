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
