def reverse_array(arr: list) -> list:
    """Reverse the elements of a list."""
    rev = []
    for i in arr:
        rev = [i] + rev
    # Or simply: return arr[::-1]
    return rev

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"Original list: {arr}")
    print(f"Reversed list: {reverse_array(arr)}")
