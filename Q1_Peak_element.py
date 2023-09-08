# Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors.
# Input: array[] = {10, 20, 15, 2, 23, 90, 67}
# Output: 20 or 90
# Explanation: The element 20 has neighbors 10 & 15, both of them are less than 20, similarly 90 has neighbors 23 and 67

# One Approach
def peak_element(arr):

    # If first and the last element is the peak element
    if len(arr) == 1:  # if the array has only one element
        return 0
    if arr[0] >= arr[1]:  # if the first element is the peak element
        return 0
    if arr[len(arr)-1] >= arr[len(arr)-2]:  # if the last element is the peak element
        return len(arr)-1

    low = 1
    while low < len(arr)-1:
        for i in range(low, low+(len(arr)-2)):
            if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                print('The index of the peak element is: ', i)
                low += 1
            else:
                low += 1
    return arr

result = peak_element([2, 25, 52, 55, 100, 250, 1000])
print(result)


# Another Approach
def find_peak_element(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return arr[left]

arr = [1, 2, 3, 5, 4, 2]
peak = find_peak_element(arr)
print("A peak element:", peak)

