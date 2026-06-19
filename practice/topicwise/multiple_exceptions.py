try:
    num = int(input())
    print(10 / num)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Zero not allowed")
