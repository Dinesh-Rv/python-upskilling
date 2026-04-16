import threading

# Without Lock

counter = 0

def increment_unsafe():
    global counter
    for _ in range(10000):
        counter += 1

print("\n=== Without Lock ===")
counter = 0

t1 = threading.Thread(target=increment_unsafe)
t2 = threading.Thread(target=increment_unsafe)
t3 = threading.Thread(target=increment_unsafe)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f"Final Counter: {counter}")
print(f"Expected: 30000")


# With Lock
counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1

print("\n=== With Lock ===")
counter = 0

t1 = threading.Thread(target=increment_safe)
t2 = threading.Thread(target=increment_safe)
t3 = threading.Thread(target=increment_safe)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f"Expected: 30000")
print(f"Got: {counter}")