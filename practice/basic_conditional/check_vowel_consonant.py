def check_character(char: str) -> str:
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
