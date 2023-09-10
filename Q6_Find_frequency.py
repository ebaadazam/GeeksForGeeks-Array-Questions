# Given a vector of N positive integers and an integer X. The task is to find the frequency of X in vector.

def find_frequency(arr, n, x):
    count = 0
    for i in arr:
        if i == x:
            count += 1
    return count

arr = [1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 6]
n = len(arr)
x = 6  # number to find the frequency
print(find_frequency(arr, n, x))
