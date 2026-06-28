try:
    num = int(input("Enter the denominator (e.g., 0): "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
