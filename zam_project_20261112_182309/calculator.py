def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculate(operation, a, b):
    ops = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
    }
    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")
    return ops[operation](a, b)
