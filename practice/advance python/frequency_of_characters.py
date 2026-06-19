def char_frequency(text: str) -> dict:
    """Calculate the frequency of each character in a string."""
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

if __name__ == "__main__":
    user_text = input("Enter a string: ")
    frequency = char_frequency(user_text)
    print("Character Frequencies:")
    for char, count in frequency.items():
        print(f"'{char}': {count}")
