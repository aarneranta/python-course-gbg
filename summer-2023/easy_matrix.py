m1 = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
m2 = [[3, 2, 1], [6, 2, 4], [9, 6, 3]]
m3 = [[1, 2], [3, 4], [5, 6]]
m4 = [[1, 2, 3], [3, 4], [5, 6]]

def lab3_format(m):
    '''
    Convert a matrix in a string in the format used in lab 3
    '''
    for row in m:
        print("\t".join([str(cell) for cell in row]))    

def ismat(m):
    '''
    Check that a list of list is actually a matrix
    '''
    n = len(m[0])
    for row in m[1:]:
        if not len(row) == n:
            return False
    return True

def matdim(m):
    '''
    Return the dimensions (nrows, ncols) of a given matrix
    '''
    return (len(m),len(m[0]))

def emptymat(nrows, ncols):
    '''
    Build an empty matrix with the given dimensions
    '''
    m = []
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(0)
        m.append(row)
    return m

def matmul_by_scalar(m, s):
    '''
    Multiply a matrix by a scalar
    '''
    if not ismat(m):
        return
    (nrows,ncols) = matdim(m1)
    n = emptymat(nrows, ncols)
    for i in range(nrows):
        for j in range(ncols):
            n[i][j] = s * m[i][j]
    return n

def matsum(m1, m2):
    '''
    Sum two matrices
    '''
    if not ismat(m1) or not ismat(m2) or not matdim(m1) == matdim(m2):
        return
    (nrows,ncols) = matdim(m1)
    m = emptymat(nrows, ncols)
    for i in range(nrows):
        for j in range(ncols):
            m[i][j] = m1[i][j] + m2[i][j]
    return m
 