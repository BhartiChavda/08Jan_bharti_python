def check_eligibility(age: int) -> bool:
    """Check if the user is eligible to vote (age >= 18)."""
    return age >= 18

if __name__ == "__main__":
    try:
        user_age = int(input("Enter your age: "))
        if user_age < 0:
            print("Age cannot be negative.")
        elif check_eligibility(user_age):
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote yet.")
    except ValueError:
        print("Invalid input! Please enter a valid age (integer).")
