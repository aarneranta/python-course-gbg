def add(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]


def subtract(arr1, arr2):
    arr2 = [[-arr2[i][j] for j in range(len(arr2[0]))] for i in range(len(arr2))]
    return add(arr1, arr2)


def print_arr(arr):
    num_len = 1
    cols, rows = len(arr[0]), len(arr)
    for i in range(rows):
        for j in range(cols):
            new_len = len(str(arr[i][j]))
            if new_len > num_len:
                num_len = new_len

    row_text = ""
    for i in range(rows):
        row_text += "["
        for j in range(cols):
            row_text += str(arr[i][j]).ljust(num_len+1) if j != cols-1 else str(arr[i][j]).ljust(num_len)
            if j == cols - 1:
                row_text += "]"
                print(row_text)
                row_text = ""


arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = [[7, 8, 9], [10, 11, 12]]
print_arr(arr2)
