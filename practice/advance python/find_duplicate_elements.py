def find_duplicates(arr: list) -> list:
    """Find duplicate elements in a list."""
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 5, 1]
    print(f"Original list: {arr}")
    print(f"Duplicate elements: {find_duplicates(arr)}")
