def is_divisible_by_5(num: int) -> bool:
    """Check if a number is divisible by 5."""
    return num % 5 == 0

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number: "))
        if is_divisible_by_5(user_num):
            print(f"{user_num} is divisible by 5")
        else:
            print(f"{user_num} is NOT divisible by 5")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
