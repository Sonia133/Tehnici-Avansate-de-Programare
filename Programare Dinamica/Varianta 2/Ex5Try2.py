def readInput():
    n = int(input())
    activs = [None] * n
    for i in range(n):
        activs[i] = [int(x) for x in input().split()]
        activs[i].append(i + 1)

    return activs, n

def getSol(activs, n):
    profit = [activs[i][0] for i in range(n)]

    for i in range(1, n):
        pMax = 0
        currTime = 0
        for j in range(i):
            if currTime + activs[j][2] <= activs[j][1] and pMax < profit[j]:
                currTime += activs[i][2]
                pMax = profit[j]
        profit[i] += pMax

    pMax = 0
    poz = -1
    activ = [0] * n

    for i in range(n):
        if pMax < profit[i]:
            pMax = profit[i]
            poz = i

    print(pMax)
    while pMax != 0:
        if pMax == profit[poz]:
            activ[poz] = 1
            pMax -= activs[poz][0]
        poz -= 1

    for i in range(n):
        if activ[i] == 1:
            print(activs[i][3], end = ' ')

def mainCode():
    activs, n = readInput()
    activs = sorted(activs, key = lambda x : x[0]/x[2], reverse = True)
    getSol(activs, n)

mainCode()