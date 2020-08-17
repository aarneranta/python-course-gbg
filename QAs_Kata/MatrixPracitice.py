def printMatrix(mat):
    for i in range(len(mat)):
        print("|", end="")
        for j in range(len(mat[0])):
            if j < len(mat[0]) - 1:
                print(mat[i][j], end="\t")
            else:
                print(mat[i][j], end="")
        print("|", end="\n")


my_mat = [[1, 2], [3, 4]]
printMatrix(my_mat)
print()

import numpy as np

s1 = [[1, 5, 7], [2, 4, 8]]
s2 = [[1, 0], [0, 1], [1, 1]]
printMatrix(np.matmul(s1, s2))
