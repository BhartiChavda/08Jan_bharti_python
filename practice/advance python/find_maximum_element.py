def find_max(arr: list):
    """Find the maximum element in a list."""
    if not arr:
        return None
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num

if __name__ == "__main__":
    arr = [12, 45, 7, 89, 34]
    print(f"List: {arr}")
    print(f"Maximum element: {find_max(arr)}")
