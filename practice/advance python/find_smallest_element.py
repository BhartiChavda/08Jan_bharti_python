def find_smallest(arr: list):
    """Find the smallest element in a list."""
    if not arr:
        return None
    small = arr[0]
    for i in arr:
        if i < small:
            small = i
    return small

if __name__ == "__main__":
    arr = [12, 5, 7, 1, 20]
    print(f"List: {arr}")
    print(f"Smallest element: {find_smallest(arr)}")
