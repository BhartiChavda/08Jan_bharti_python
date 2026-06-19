def remove_spaces(text: str) -> str:
    """Remove all spaces from a given string."""
    return text.replace(" ", "")

if __name__ == "__main__":
    user_text = input("Enter a string with spaces: ")
    print(f"String without spaces: '{remove_spaces(user_text)}'")
