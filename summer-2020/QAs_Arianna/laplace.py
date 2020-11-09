from matprint import matprint

def minor(m,i,j):
  '''
  compute a minor of a matrix
  input: a matrix m,
         the index i of the row to exclude,
         the index j of the column to exclude
  output: a submatrix of m without row i and row j
  '''
  minor = [row[:j] + row[j+1:] for row in (m[:i] + m[i + 1:])]
  matprint(minor)
  return minor

def determinant(m):
    '''
    compute the determinant of a matrix
    input: a matrix m
    output: a scalar
    '''
    if len(m) == 2: # base case (ad - bc) (assuming the matrix is squared)
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for j in range(len(m)):
        # sign * j-th el of row 0* determinant of minor excluding row 0, col j
        det += ((-1)**j) * m[0][j] * determinant(minor(m,0,j))
        print("\n")
    return det

if __name__ == "__main__":
    m = [[1,2,3], [4,5,6], [7,8,9]]
    matprint(m)
    print(determinant(m))
    