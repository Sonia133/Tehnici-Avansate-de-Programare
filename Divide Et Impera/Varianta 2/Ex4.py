import math


def readInput():
    n = int(input())
    arr = [None] * n
    for i in range(n):
        arr[i] = [int(x) for x in input().split()]

    return arr


def findDistance(arr, i, j):
    dist = math.sqrt((arr[i][0] - arr[j][0]) * (arr[i][0] - arr[j][0]) + (arr[i][1] - arr[j][1]) * (arr[i][1] - arr[j][1]))
    return dist


def getSol(arrX, arrY, n):
    if n <= 3:
        dMin = 500
        for i in range(n):
            for j in range(i + 1, n):
                if findDistance(arrX, i, j) < dMin:
                    dMin = findDistance(arrX, i, j)
        return dMin

    median = n // 2
    medPoint = arrX[median][0]
    distLeft = getSol(arrX[:median], arrY, median -1)
    distRight = getSol(arrX[median + 1:], arrY, (n - median) - 1)

    if distLeft < distRight:
        dist = distLeft
    else:
        dist = distRight

    middle = [None] * n
    cntMiddle = 0
    for i in range(n):
        if abs(arrY[i][0] - medPoint) < dist:
            middle[cntMiddle] = arrY[i]
            cntMiddle += 1

    for i in range(cntMiddle):
        for j in range(i + 1, min(cntMiddle, i + 8)):
            if findDistance(middle, i, j) < dist:
                dist = findDistance(middle, i, j)

    return dist


def mainCode():
    arr = readInput()
    arrX = sorted(arr, key=lambda x: (x[0], x[1]))
    arrY = sorted(arr, key=lambda x: (x[1], x[0]))

    dist = getSol(arrX, arrY, len(arr))
    print(dist)


mainCode()
