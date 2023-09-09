# Given a random set of numbers, Print them in sorted order.

# Here I am using bubble sort to sort this array but this is taking way too much time
def sort_array(arr):
    for i in range(len(arr)-1):

        for j in range(len(arr)-i-1):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

arr = [5, 3, 4, 1, 2]
print('The sorted array:', sort_array(arr))


# Using Merge Sort to sort this array
def sortArr(arr, n):
    if n > 1:
        mid = n // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        sortArr(left_half, len(left_half))
        sortArr(right_half, len(right_half))

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

arr = [3, 1, 4, 2]
n = len(arr)
print('The sorted array: ', sortArr(arr, n))

