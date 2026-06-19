def is_leap_year(year: int) -> bool:
    """Check if a given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if __name__ == "__main__":
    try:
        user_year = int(input("Enter year: "))
        if is_leap_year(user_year):
            print(f"{user_year} is a Leap Year")
        else:
            print(f"{user_year} is Not a Leap Year")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
