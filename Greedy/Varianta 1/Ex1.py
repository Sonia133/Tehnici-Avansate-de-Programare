def readInput() :
    a, b = [int(i) for i in input().split()]
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append([int(x) for x in input().split()])
    return a, b, n, arr

def getSol(a, b, arr) :
    if arr[0][0] <= a:
        tmp = arr[0]
    else:
        return 0

    sol = []
    for int in arr:
        if int[0] <= a:
            if int[1] > tmp[1]:
                    tmp = int
        else:
            sol.append(tmp)
            a = tmp[1]
            tmp = int

    if sol[len(sol) - 1][1] < b:
        if tmp[1] >= b:
            sol.append(tmp)
        else:
            return 0

    return sol

def driveCode() :
    a, b, n, arr = readInput()
    arr = sorted(arr, key = lambda x: (x[0], x[1]))
    sol = getSol(a, b, arr)
    if sol :
        print(sol)
    else:
        print(-1)

driveCode()