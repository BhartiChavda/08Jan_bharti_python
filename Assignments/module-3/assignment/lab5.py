#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input). 

try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation: +, -, *, /")
    operator = input("Enter operator: ")

   
    if operator == "+":
        result = num1+num2
        print(f"Result:{num1}+{num2}={result}")

    elif operator == "-":
        result = num1-num2
        print(f"Result:{num1}-{num2}={result}")

    elif operator == "*":
        result = num1*num2
        print(f"Result:{num1}*{num2}={result}")

    elif operator == "/":
        result = num1/num2
        print(f"Result:{num1}/{num2}={result}")

    else:
        print("Invalid operator! Please select +, -, *, or /")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Calculator program executed successfully.")

#  Write a Python program to demonstrate handling multiple exceptions. 

try:
    
    file = open("data.txt", "r")
    content = file.read()
    print("File Content:\n", content)

    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
    print("Result of 10 divided by", num, "is", result)

except FileNotFoundError:
    print("Error: The file 'data.txt' was not found!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter a valid number.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Program executed successfully.")