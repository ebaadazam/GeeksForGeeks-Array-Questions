# Given an array, rotate the array by one position in clock-wise direction. Assign every element with its previous
# element and first element with the last element.

def rotate(arr, n):
    last_elem = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_elem
    return arr

arr = [1, 2, 3, 4, 5]
n = len(arr)
print(rotate(arr, n))
