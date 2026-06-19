def count_case(text: str) -> tuple:
    """Count the number of uppercase and lowercase letters in a string."""
    upper = sum(1 for ch in text if ch.isupper())
    lower = sum(1 for ch in text if ch.islower())
    return upper, lower

if __name__ == "__main__":
    user_text = input("Enter a string: ")
    upper_count, lower_count = count_case(user_text)
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")
