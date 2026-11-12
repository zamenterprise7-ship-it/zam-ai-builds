import sys
from calculator import calculate

def print_help():
    print("Usage: python main.py <operation> <num1> <num2>")
    print("Operations: add, subtract, multiply, divide")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_help()
        sys.exit(1)
    op, a_str, b_str = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        a, b = float(a_str), float(b_str)
        result = calculate(op, a, b)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
