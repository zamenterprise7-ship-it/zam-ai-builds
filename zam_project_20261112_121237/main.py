def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else None


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ").strip()
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
            if result is None:
                print("Error: Division by zero.")
                return
        else:
            print("Invalid operation.")
            return
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()