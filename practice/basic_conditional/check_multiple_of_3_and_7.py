def check_multiple(num: int) -> bool:
    """Check if a number is a multiple of both 3 and 7."""
    return num % 3 == 0 and num % 7 == 0

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number: "))
        if check_multiple(user_num):
            print(f"{user_num} is a multiple of both 3 and 7")
        else:
            print(f"{user_num} is NOT a multiple of both 3 and 7")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
