def check_result(marks: float) -> str:
    """Check if a student is pass or fail (passing marks = 35)."""
    if marks < 0 or marks > 100:
        return "Invalid marks (Must be between 0 and 100)"
    elif marks >= 35:
        return "Pass"
    else:
        return "Fail"

if __name__ == "__main__":
    try:
        user_marks = float(input("Enter marks: "))
        print(f"Result: {check_result(user_marks)}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
