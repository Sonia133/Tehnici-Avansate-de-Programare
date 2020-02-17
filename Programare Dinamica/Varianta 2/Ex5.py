def readInput():
    n = int(input())
    activs = [None] * n
    for i in range(n):
        activs[i] = [int(x) for x in input().split()]
        activs[i].append(i + 1)

    return activs, n

def getSol(activs, n):
    currTime = 0
    profitTotal = 0

    for i in range(n):
        if currTime + activs[i][2] <= activs[i][1]:
            print(activs[i][3], end = ' ')
            currTime += activs[i][2]
            profitTotal += activs[i][0]

    print()
    print(profitTotal)

def mainCode():
    activs, n = readInput()
    activs = sorted(activs, key = lambda x : x[0]/x[2], reverse = True)
    getSol(activs, n)

mainCode()