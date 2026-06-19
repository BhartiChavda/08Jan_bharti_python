def is_palindrome(text: str) -> bool:
    """Check if a given string is a palindrome."""
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    user_text = input("Enter a string: ")
    if is_palindrome(user_text):
        print(f"'{user_text}' is a Palindrome")
    else:
        print(f"'{user_text}' is Not a Palindrome")
