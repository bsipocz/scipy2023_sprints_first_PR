def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_prime(value):
    if value < 2:
        raise ValueError(f"Don't pass any numbers smaller than 2. Received {value}.")
    elif value == 2:
        return True
    
    current_val = 2
    while current_val < value:
        if value % current_val == 0:
            return False
        
        current_val += 1
    return True