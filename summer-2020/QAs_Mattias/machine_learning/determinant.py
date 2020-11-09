from numpy import array, delete


# This return a subarray.
def sub_arr(arr, j):
    return delete(arr[1:], j, 1)


def determinant(arr):
    if arr.shape[0] == 1:
        return arr[0, 0]
    elif arr.shape[0] == 2:
        return arr[0, 0] * arr[1, 1] - arr[1, 0] * arr[0, 1]
    else:
        det = 0
        for j in range(arr.shape[0]):
            det += ((-1) ** j) * arr[0, j] * determinant(sub_arr(arr, j))
        return det


arr = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(determinant(arr))
arr = array([[7, 1, 3], [6, 4, 2], [5, 8, 9]])
print(determinant(arr))