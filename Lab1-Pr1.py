def copy_values(arr1, arr2, start_position):
    if start_position > len(arr1):
        raise ValueError("Start position is greater than the length of the first array")

    for i, value in enumerate(arr2):
        arr1.insert(start_position + i, value)

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
start_position = 2
copy_values(arr1, arr2, start_position)
print(arr1)