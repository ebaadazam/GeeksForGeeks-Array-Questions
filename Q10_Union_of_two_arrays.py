'''Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union
between these two arrays.
Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are
repetitions, then only one occurrence of element should be printed in the union.
Note : Elements are not necessarily distinct.
'''


# One Approach
# This code is taking way too much time to execute as per Geeks for Geeks
a = [1, 2, 3, 4]
b = [2, 3, 4, 5, 6, 7]
arr = []
for i in a:
    if i not in arr:
        arr.append(i)
for i in b:
    if i not in arr:
        arr.append(i)
c = 0
for i in range(len(arr)):
    c += 1
print('The Array is: ', arr)
print('The length of the Union of Array is: ', c)



# So Here is the alternative Approach
a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
m, n = len(a), len(b)
i, j = 0, 0
arr = []

while i < m and j < n:
    if a[i] < b[j]:
        arr.append(a[i])
        i += 1
    elif a[i] > b[j]:
        arr.append(b[j])
        j += 1
    elif a[i] == b[j]:
        arr.append(b[j])
        i += 1
        j += 1
while i < m:
    arr.append(a[i])
    i += 1
while j < n:
    arr.append(b[j])
    j += 1
print('The Array is: ', arr)
print('The length of the Union of Array is: ', len(arr))