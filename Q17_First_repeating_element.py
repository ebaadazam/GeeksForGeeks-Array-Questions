'''
Given an array arr[] of size n, find the first repeating element. The element should occur more than once and the
index of its first occurrence should be the smallest.
Note:- The position you return should be according to 1-based indexing
'''


# One Approach
arr = [7, 4, 0, 9, 4, 8, 8, 2, 4, 5, 5, 1]
rep = []
non_rep = []  # to store the elements getting repeated
for i in arr:
    if i in rep:
        non_rep.append(i)
    rep.append(i)
print(sorted(list(set(non_rep))))  # these are the elements which are getting repeated

this = non_rep[0] # contains the first repeated element
for i in range(1, len(arr)):
    if arr[i] == this:
        print(i+1)  # the first repeated element is at the location 2 (1-based indexing)
        break


# Another Approach
def first_repeating(arr):
    min_index = float('inf') # float('inf') is a way to represent positive infinity in Python. It is larger than any
    # other number, so it is often used as an initial value when searching for a minimum value. In the code above,
    # min_index is initialized to float('inf') so that any index found later in the code will be smaller than this
    # initial value and will update the value of min_index.
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict.keys():
            min_index = min(min_index, dict[arr[i]])
        else:
            dict[arr[i]] = i
    if min_index == float('inf'):
        return -1
    else:
        return min_index + 1

arr = [1, 2, 3, 5, 4, 5, 6]
print(first_repeating(arr))
