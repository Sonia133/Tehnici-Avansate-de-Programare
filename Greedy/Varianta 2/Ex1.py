def readInput():
    n, p = [int(i) for i in input().split()]
    arr = [None] * n
    for i in range(n):
        arr[i] = ([int(x) for x in input().split()])
        arr[i].append(i + 1)
    return n, arr


def getSol(n, arr):
    count, h = 0, 0
    sol = []
    lastColor = -1

    for x in arr:
        if lastColor == -1:
            lastColor = x[1]
            count += 1
            h += x[0]
            sol.append(x)
        else:
            if lastColor != x[1]:
                count += 1
                h += x[0]
                sol.append(x)
                lastColor = x[1]

    return count, h, sol


def driveCode():
    n, arr = readInput()
    arr = sorted(arr, key = lambda x: x[0], reverse = True)
    count, h, sol = getSol(n, arr)

    print(count, end=' ')
    print(h)
    for x in sol:
        print(x[2], end=' ')


driveCode()
