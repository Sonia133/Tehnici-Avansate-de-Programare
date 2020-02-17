def readInput():
    n, p = [int(x) for x in input().split()]
    towers = [None] * n
    for i in range(n):
        towers[i] = [int(x) for x in input().split()]

    return towers

def getSol(T, n):
    L = [1] * n
    prev = [1] * n
    for i in range(1, n):
        for j in range(i):
            if T[i][0] != T[j][0] and T[i][1] != T[j][1] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1
                prev[i] = j

    pozMax = 0

    for i in range(1, n):
        if L[pozMax] < L[i]:
            pozMax = i

    valMax = L[pozMax]

    while valMax > 0:
        print(T[pozMax])
        pozMax = prev[pozMax]
        valMax -= 1

def mainCode():
    towers = readInput()
    towers = sorted(towers, key = lambda x: x[0], reverse = True)
    getSol(towers, len(towers))

mainCode()