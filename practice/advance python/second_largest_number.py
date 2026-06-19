def get_second_largest(arr: list):
    """Find the second largest number in a list."""
    if len(arr) < 2:
        return None
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return None
    unique_arr.sort()
    return unique_arr[-2]

if __name__ == "__main__":
    arr = [10, 20, 4, 45, 99, 99]
    print(f"List: {arr}")
    print(f"Second largest element: {get_second_largest(arr)}")
