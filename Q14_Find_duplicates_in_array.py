'''
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than
 once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1].
'''

# One Approach
arr = [1, 2, 3, 4, 5, 6, 8, 5, 4, 3]
new_arr = []
num = []
found = False
for i in range(len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])
    else:
        num.append(arr[i])
        found = True
if found:
    print(sorted(num))
else:
    print(-1)  # if no occurrence is found then print -1



# Another Approach
def duplicates(arr, n):
    seen = set()  # To keep track of seen elements
    duplicates = set()  # To store duplicate elements

    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    if not duplicates:
        return [-1]

    return sorted(duplicates)

arr = [5, 3, 1, 3, 2, 2]
n = len(arr)
print(duplicates(arr, n))

