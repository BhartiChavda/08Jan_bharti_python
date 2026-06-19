def check_sign(num: float) -> str:
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
        print(f"The number is {check_sign(user_num)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
