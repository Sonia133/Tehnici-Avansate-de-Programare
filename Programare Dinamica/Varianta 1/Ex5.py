def readInput():
    n = int(input())
    activ = [None] * n
    for i in range(n):
        activ[i] = [int(x) for x in input().split()]

    return activ, n

def getSol(activSorted, n):
    L = [0] * n

    for i in range(n):
        L[i] = activSorted[i][2]

    for i in range(1, n):
        pMax = 0
        for j in range(i):
            if activSorted[j][1] <= activSorted[i][0] and pMax < L[j]:
                pMax = L[j]
        L[i] = activSorted[i][2] + pMax

    pMax = 0
    poz = -1
    activs = [0] * n

    for i in range(n):
        if pMax < L[i]:
            pMax = L[i]
            poz = i

    print(pMax)
    while pMax != 0:
        if pMax == L[poz]:
            activs[poz] = 1
            pMax -= activSorted[poz][2]
        poz -= 1

    for i in range(n):
        if activs[i] == 1:
            print(activSorted[i][0], end = ' ')
            print(activSorted[i][1])

def mainCode():
    activ, n = readInput()
    activSorted = sorted(activ, key = lambda x : x[1])
    getSol(activSorted, n)


mainCode()