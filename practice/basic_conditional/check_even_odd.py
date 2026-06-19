def check_even_odd(num: int) -> str:
    """Check if a number is even or odd."""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number: "))
        print(f"The number {user_num} is {check_even_odd(user_num)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
