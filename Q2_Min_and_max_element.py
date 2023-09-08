# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array

def max_elem(arr):
    max_no = 0
    for i in arr:
        if i > max_no:
            max_no = i
    return f'The maximum element in the array: {max_no}'

def min_elem(arr):
    min_no = arr[0]
    for i in arr:
        if i < min_no:
            min_no = i
    return f'The minimum element in the array: {min_no}'

arr = [10, 444, 34, 322, 12, 15]
print(max_elem(arr))
print(min_elem(arr))