def merge_lists(list1: list, list2: list) -> list:
    """Merge two lists into one."""
    return list1 + list2

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(f"List 1: {a}")
    print(f"List 2: {b}")
    print(f"Merged list: {merge_lists(a, b)}")
