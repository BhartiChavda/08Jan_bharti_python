import os

files_content = {
    'check_positive_negative_zero.py': '''def check_number(num: float) -> str:
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
        print(f"The number {user_num} is {check_number(user_num)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
''',

    'check_even_odd.py': '''def check_even_odd(num: int) -> str:
    """Check if a number is even or odd."""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    try:
        user_num = int(input("Enter a number: "))
        print(f"The number {user_num} is {check_even_odd(user_num)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
''',

    'check_voting_eligibility.py': '''def check_eligibility(age: int) -> bool:
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
''',

    'find_larger_number.py': '''def find_larger(num1: float, num2: float) -> str:
    """Find the larger of two numbers."""
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num2 > num1:
        return f"{num2} is larger than {num1}"
    else:
        return "Both numbers are equal"

if __name__ == "__main__":
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        print(find_larger(n1, n2))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
''',

    'check_divisible_by_5.py': '''def is_divisible_by_5(num: int) -> bool:
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
''',

    'check_leap_year.py': '''def is_leap_year(year: int) -> bool:
    """Check if a given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if __name__ == "__main__":
    try:
        user_year = int(input("Enter a year: "))
        if user_year <= 0:
            print("Please enter a valid positive year.")
        elif is_leap_year(user_year):
            print(f"{user_year} is a Leap Year")
        else:
            print(f"{user_year} is Not a Leap Year")
    except ValueError:
        print("Invalid input! Please enter a valid integer year.")
''',

    'check_vowel_consonant.py': '''def check_character(char: str) -> str:
    """Check if a character is a vowel or consonant."""
    if not char.isalpha() or len(char) != 1:
        return "Invalid input (Please enter a single alphabet)"
        
    char_lower = char.lower()
    if char_lower in "aeiou":
        return "Vowel"
    else:
        return "Consonant"

if __name__ == "__main__":
    user_char = input("Enter a single character: ").strip()
    result = check_character(user_char)
    print(f"The character '{user_char}' is a {result}")
''',

    'check_pass_fail.py': '''def check_result(marks: float) -> str:
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
''',

    'check_weather.py': '''def check_weather(temp: float) -> str:
    """Determine weather condition based on temperature."""
    if temp < 15:
        return "Cold"
    elif temp <= 35:
        return "Normal"
    else:
        return "Hot"

if __name__ == "__main__":
    try:
        user_temp = float(input("Enter temperature in Celsius: "))
        print(f"The weather is {check_weather(user_temp)}")
    except ValueError:
        print("Invalid input! Please enter a valid temperature.")
''',

    'check_multiple_of_3_and_7.py': '''def check_multiple(num: int) -> bool:
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
'''
}

target_dir = r"d:\TopsPython\practice\basic_conditional"

for filename, content in files_content.items():
    filepath = os.path.join(target_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully created {len(files_content)} files in {target_dir}")
