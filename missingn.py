def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    sum_of_elements = sum(arr)
    return total - sum_of_elements

print(find_missing_number([1, 2, 4, 6, 3, 7, 8]))  
