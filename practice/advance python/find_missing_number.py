def find_missing(arr: list, n: int) -> int:
    """Find the missing number in a continuous sequence from 1 to n."""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    n = 5
    print(f"List: {arr}")
    print(f"Missing number (from 1 to {n}): {find_missing(arr, n)}")
