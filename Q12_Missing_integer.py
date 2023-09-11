# Given an array arr[] of size N-1 with integers in the range of [1, N]. The task is to find the missing number from
# the first N integers.

def missing(arr):
    n = len(arr)+1

    # Formula for getting sum of n natural numbers
    actual_sum = (n*(n+1))//2

    # Actual sum of the array
    arr_sum = sum(arr)

    return actual_sum - arr_sum

arr = [1, 2, 3, 5]
print('The missing number in', arr, 'is', missing(arr))