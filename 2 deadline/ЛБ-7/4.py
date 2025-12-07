call_counter = 0

def increment_counter():
    """Увеличивает счетчик вызовов на 1"""
    global call_counter
    call_counter += 1


increment_counter()
increment_counter()
increment_counter()
print(call_counter)  