def readInput():
    n, k = [int(x) for x in input().split()]
    arr = [None] * n
    for i in range(n):
        arr[i] = [int(x) for x in input().split()]

    return arr, n, k

def getSol(arr, n, k):
    findK = [[0 for i in range(k + 1)] for j in range(n)]
    for i in range(len(arr[0])):
        findK[0][arr[0][i]] = arr[0][i]

    for i in range(1,n):
        for j in range(len(arr[i])):
            for t in range(k + 1):
                if findK[i - 1][t] != 0:
                    if t + arr[i][j] < 12:
                        findK[i][t + arr[i][j]] = arr[i][j]

    i = n - 1
    if findK[n - 1][k] != 0:
        while(k > 0):
            print(findK[i][k], end = " ")
            print('din sirul ' + str(i + 1))
            k -= findK[i][k]
            i -= 1

def mainCode():
    arr, n, k = readInput()
    getSol(arr, n, k)

mainCode()