# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.

# One way
def common_element(A, B, C, n1, n2, n3):
    i, j, k = 0, 0, 0
    common = []
    while (i < n1) and (j < n2) and (k < n3):
        if A[i] == B[j]:
            common.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1
    return common

A = [-44, 1, 5, 10, 20, 40, 80]
B = [-76, -44, -33, 6, 7, 20, 80, 100]
C = [-44, 3, 4, 15, 20, 30, 70, 80, 120]
n1, n2, n3 = len(A), len(B), len(C)
print(common_element(A, B, C, n1, n2, n3))



# Another Way
def common_element2(A, B, C, n1, n2, n3):
    i, j, k = 0, 0, 0

    last = -12345678  # variable to store last common element
    res = []  # list to store the common elements

    while i < n1 and j < n2 and k < n3:

        if A[i] == B[j] == C[k]:

            # checking if the common element is not already present
            if last != A[i]:
                res.append(A[i])  # adding the common element to the result list
                last = A[i]  # updating the last common element
            i += 1
            j += 1
            k += 1

        # if the minimum element is from the first array
        elif min(A[i], B[j], C[k]) == A[i]:
            i += 1

        # if the minimum element is from the second array
        elif min(A[i], B[j], C[k]) == B[j]:
            j += 1

        # if the minimum element is from the third array
        else:
            k += 1
    return res

A = [-69, -68, -39, -25, -6, 18, 33, 39, 42, 46, 52, 55, 55, 64, 71]
B = [-97, -92, -90, -90, -87, -85, -82, -77, -77, -77, -75, -71, -67, -64, -60, -59, -58, -52, -49, -48, -48, -47, -47, -46, -41, -36, -35, -29, -28, -26, -25, -20, -19, -14, -13, -13, -11, -10, -6, -4, 2, 3, 9, 12, 15, 17, 20, 22, 23, 24, 27, 29, 36, 36, 37, 38, 39, 42, 45, 47, 48, 48, 50, 52, 52, 53, 57, 59, 60, 63, 63, 64, 64, 65, 68, 70, 71, 76, 76, 77, 83, 83, 84, 85, 86, 89, 97, 97]
C = [-95, -95, -86, -83, -70, -67, -57, -53, -52, -35, -33, -32, -30, -20, -16, -15, -15, -11, -10, -10, -4, 0, 4, 15, 18, 34, 36, 37, 39, 41, 43, 43, 48, 49, 50, 51, 58, 63, 64, 67, 69, 77, 79, 84, 84, 94, 95, 97]
n1, n2, n3 = len(A), len(B), len(C)
print(common_element2(A, B, C, n1, n2, n3))

