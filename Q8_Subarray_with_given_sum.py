''' Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a
 given number S and return the left and right index(1-based indexing) of that sub-array.
In case of multiple sub-arrays, return the sub-array indexes which come first on moving from left to right.
Note:- You have to return an ArrayList consisting of two elements left and right. In case no such sub-array exists
return an array consisting of element -1. '''


def sub_array_sum(arr, n, s):
    left = 0
    right = 0
    current_sum = arr[0]
    is_found = False

    while right < len(arr):
        if current_sum == s:
            is_found = True
            break

        elif current_sum < s:
            right += 1
            if right < len(arr):
                current_sum += arr[right]

        elif current_sum > s:
            current_sum -= arr[left]
            left += 1

    if is_found:
        return i+1, j+1
    return -1

arr = [142, 112, 54, 69, 148, 45, 63, 158, 38, 60, 124, 142, 130, 179, 117, 36, 191, 43, 89, 107, 41, 143, 65, 49, 47,
       6, 91, 130, 171, 151, 7, 102, 194, 149, 30, 24, 85, 155, 157, 41, 167, 177, 132, 109, 145, 40, 27, 124, 138, 139,
       119, 83, 130, 142, 34, 116, 40, 59, 105, 131, 178, 107, 74, 187, 22, 146, 125, 73, 71, 30, 178, 174, 98, 113]
s = 665
n = len(arr)
print(sub_array_sum(arr, n, s))