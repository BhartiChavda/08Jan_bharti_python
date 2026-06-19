def find_common(list1: list, list2: list) -> list:
    """Find common elements between two lists."""
    common = [item for item in list1 if item in list2]
    # Alternatively: return list(set(list1) & set(list2))
    return common

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    print(f"List 1: {a}")
    print(f"List 2: {b}")
    print(f"Common elements: {find_common(a, b)}")
