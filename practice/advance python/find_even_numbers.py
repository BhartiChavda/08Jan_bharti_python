def get_even_numbers(arr: list) -> list:
    """Find and return all even numbers from a list."""
    return [i for i in arr if i % 2 == 0]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(f"Original list: {arr}")
    print(f"Even numbers: {get_even_numbers(arr)}")
