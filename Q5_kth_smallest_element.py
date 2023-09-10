# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest
# element in the given array. It is given that all array elements are distinct.
# Note:  l and r denotes the starting and ending index of the array.

def kthSmallest(arr, l, r, k):
    if (k < 1) or (k > r - l + 1):
        return None
    return quick_select(arr, l, r, k - 1)

def partition(arr, low, high):
    pivot = arr[high]  # pivot as the last element of the array
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return i + 1

def quick_select(arr, low, high, k):
    if low < high:
        pivot_index = partition(arr, low, high)

        # If the pivot index is equal to k, then the pivot element is returned as it is the k-th smallest element
        if pivot_index - low == k:
            return arr[pivot_index]

        # If the pivot index is less than k, then we know that the k-th smallest element lies in the right sub-array,
        elif pivot_index - low < k:
            return quick_select(arr, pivot_index + 1, high, k - (pivot_index - low + 1))

        # If the pivot index is greater than k, then we know that the k-th smallest element lies in the left sub-array
        else:
            return quick_select(arr, low, pivot_index - 1, k)
    else:
        return arr[low]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthSmallest(arr, 0, len(arr)-1, k))