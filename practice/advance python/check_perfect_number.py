def is_perfect_number(num: int) -> bool:
    """Check if a given number is a perfect number."""
    if num <= 0:
        return False
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisor_sum == num

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number: "))
        if is_perfect_number(user_num):
            print(f"{user_num} is a Perfect Number")
        else:
            print(f"{user_num} is Not a Perfect Number")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
