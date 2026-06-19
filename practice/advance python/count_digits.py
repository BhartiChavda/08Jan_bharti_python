def count_digits(num: int) -> int:
    """Count the number of digits in an integer."""
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number: "))
        print(f"Total Digits in {user_num}: {count_digits(user_num)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
