'''
Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).
'''

class Sort:
    # Function to sort a list using quick sort algorithm.
    def quick_sort(self, arr, low, high):
        if low < high:

            # Divide the array into two halves
            pivot = self.partition(arr, low, high)

            # Sort the two halves recursively
            self.quick_sort(arr, low, pivot - 1)
            self.quick_sort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        # Swap arr[i+1] and arr[high] to place the pivot in the correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

arr = [4, 5, 1, 3, 2]
n = len(arr)
obj = Sort()
obj.quick_sort(arr, 0, n - 1)

for i in range(n):
    print(arr[i], end=" ")
print()