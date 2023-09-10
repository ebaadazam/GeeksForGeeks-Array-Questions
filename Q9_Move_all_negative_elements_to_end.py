''' Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative
element at the end of array without changing the order of positive element and negative element.

Input we entered      - [1, -1, 3, 2, -7, -5, 11, 6]
Output should be like - [1  3  2  11  6  -1  -7  -5] '''

# One Approach
def neg_int(arrr, n):
    pos = list()
    neg = list()
    for i in range(n):
        if arrr[i] > 0:
            pos.append(arrr[i])
        else:
            neg.append(arrr[i])
    return pos+neg

arrr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arrr)
print(neg_int(arrr, n))


# Another Approach
# Here where we are returning the same array in which the elements were stored earlier which was not the case with the above one.
def func(arr, n):
    new_arr = list()

    # If elements are more than 0, append them to new arr
    for i in range(n):
        if arr[i] > 0:
            new_arr.append(arr[i])

    # If elements are less than 0, append them to new arr
    for i in range(n):
        if arr[i] < 0:
            new_arr.append(arr[i])

    # Transferring all the elements back to the original array
    for i in range(n):
        arr[i] = new_arr[i]

    return arr

arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
print(func(arr, n))