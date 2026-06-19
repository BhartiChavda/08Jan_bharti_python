def check_number(num: float) -> str:
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    try:
        user_num = float(input("Enter a number: "))
        print(f"The number {user_num} is {check_number(user_num)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
