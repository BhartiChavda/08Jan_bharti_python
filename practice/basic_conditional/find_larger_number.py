def find_larger(num1: float, num2: float) -> str:
    """Find the larger of two numbers."""
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num2 > num1:
        return f"{num2} is larger than {num1}"
    else:
        return "Both numbers are equal"

if __name__ == "__main__":
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        print(find_larger(n1, n2))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
