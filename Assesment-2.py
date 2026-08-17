def find_missing_number(arr):
    n = len(arr)
    result = 0

    for i in range(1, n + 2):
        result ^= i

    for num in arr:
        result ^= num

    return result


arr = list(map(int, input("Enter numbers: ").split()))
print("Missing number:", find_missing_number(arr))