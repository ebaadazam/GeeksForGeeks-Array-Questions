# Find the first non-repeating element in a given array arr of N integers.
# Note: Array consists of only positive and negative integers and not zero

# One Approach (Working fine but taking too much time)
arr = [-1, 2, -1, 3, 2]
def first_non_repeating(arr):
    arr_rep = []
    arr_notrep = []
    for i in range(len(arr)):
        if arr[i] in arr_rep:
            arr_notrep.append(arr[i])
        arr_rep.append(arr[i])
    for i in arr_notrep:
        for j in arr_rep:
            if i == j:
                arr_rep.remove(i)
    if arr_rep:
        return arr_rep[0]
    return 0

# Another Approach (Working better than the above approach)
def abc(arr):
    dict = {}
    new = []
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    #print(dict)
    for i in dict.items():
        if i[1] <= 1:
            new.append(i[0])
            break
    return new

arr = [17, -12, 8, 16, -17, -13, -14, -3, -6, -5, -11, -10, -12, -5, 19, -17, -5, -1, 12]
print(abc(arr))


# Another Approach (Best Approach)
def firstNonRepeating(arr):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict.keys():
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
    #print(dict)
    for i in range(len(arr)):
        if dict[arr[i]] == 1:
            return arr[i]
    return None

arr = [17, -12, 8, 16, -17, -13, -14, -3, -6, -5, -11, -10, -12, -5, 19, -17, -5, -1, 12]
print(firstNonRepeating(arr))
