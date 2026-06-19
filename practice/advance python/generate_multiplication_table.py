def generate_table(num: int, up_to: int = 10):
    """Generate and print a multiplication table for a given number."""
    for i in range(1, up_to + 1):
        print(f"{num} x {i} = {num * i}")

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number for its multiplication table: "))
        print(f"--- Multiplication Table for {user_num} ---")
        generate_table(user_num)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
