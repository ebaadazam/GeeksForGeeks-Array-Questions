# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# One Approach
def sort(arr):
    zeros, ones, twos = 0, 0, 0
    for no in arr:
        if no == 0:
            zeros += 1
        elif no == 1:
            ones += 1
        elif no == 2:
            twos += 1

    result = []
    for i in range(zeros):
        result.append(0)
    for i in range(ones):
        result.append(1)
    for i in range(twos):
        result.append(2)
    return result

print(sort([0, 2, 1, 2, 0]))



# Another Approach
def sort2(arr, n):
    low = 0
    high = n - 1
    mid = 0

    while mid <= high:

        # if element at mid is 0, swap with element at low and move both pointers.
        if arr[mid] == 0:
            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp
            mid += 1
            low += 1

        # if element at mid is 1, move mid pointer.
        elif arr[mid] == 1:
            mid += 1

        # if element at mid is 2, swap with element at high and move high pointer.
        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -= 1
    return arr

arr = [2, 0, 0, 1, 1, 2]
print(sort2(arr, len(arr)))