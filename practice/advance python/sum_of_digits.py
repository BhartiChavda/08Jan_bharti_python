def calculate_digit_sum(num: int) -> int:
    """Calculate the sum of digits of a given number."""
    num = abs(num)
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number: "))
        print(f"Sum of digits in {user_num}: {calculate_digit_sum(user_num)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
