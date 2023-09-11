# Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array
# whose sum is equal to K.

# One Approach
# This code is taking way too much time to execute as per geeks for geeks
arr = [1, 5, 5, 5, 5, 7]
sum = 10
n = len(arr)
count = 0
for i in range(n):
    for j in range(i+1, n):
        if (arr[i] + arr[j]) == sum:
            new_tuple = (arr[i], arr[j], )
            print(new_tuple)
            count += 1
print(count)


# Another Approach with much less time
def count_pairs(arr, K):
    num_freq = {}  # Dictionary to store the frequency of each number in the array
    count = 0

    # Count the frequency of each number in the array
    for num in arr:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1

    # Count the pairs with sum equal to K
    for num in arr:
        complement = K - num  # Find the complement needed for the sum to be K

        if complement in num_freq:
            count += num_freq[complement]  # Add the frequency of complement to the count

        # Special case: if complement is equal to num, then we need to subtract 1 from count
        if complement == num:
            count -= 1

    # Since each pair is counted twice, divide the count by 2 to get the actual number of pairs
    return count // 2

arr = [1, 5, 7, -1, 5]
K = 6
result = count_pairs(arr, K)
print("Number of pairs with sum", K, ":", result)
