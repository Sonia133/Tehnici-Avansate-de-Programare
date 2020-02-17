def readInput():
    n, m = [int(x) for x in input().split()]
    matrix = [None] * n
    for i in range(n):
        matrix[i] = [int(x) for x in input().split()]

    return matrix, n, m

def getSol(n, m , matrix):
    matrixValue = [[0 for j in range(m)] for i in range(n)]
    matrixValue[0][0] = matrix[0][0]
    for i in range(1, n):
        matrixValue[i][0] = matrix[i][0] + matrix[i - 1][0]

    for j in range(1, m):
        matrixValue[0][j] = matrix[0][j] + matrix[0][j - 1]

    for i in range(1, n):
        for j in range(1, m):
            matrixValue[i][j] = matrix[i][j] + max(matrixValue[i - 1][j], matrixValue[i][j - 1])

    print(matrixValue[n - 1][m - 1])
    i, j = n - 1, m - 1

    while i > 0 and j > 0:
        print(i + 1, end = " ")
        print(j + 1)
        if (matrixValue[i][j] - matrix[i][j]) == matrixValue[i - 1][j]:
            i -= 1
        else:
            j -= 1

    while i > 0:
        print(i + 1, end = " ")
        print(j + 1)
        i -= 1

    while j > 0:
        print(i + 1, end = " ")
        print(j + 1)
        j -= 1

    print(i + 1, end = " ")
    print(j + 1)

def mainCode():
    matrix, n, m = readInput()
    getSol(n, m, matrix)

mainCode()

