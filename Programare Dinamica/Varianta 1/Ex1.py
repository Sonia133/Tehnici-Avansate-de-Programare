def readInput():
    n = int(input())
    dominos = [None] * n
    for i in range(n):
        dominos[i] = [int(x) for x in input().split()]

    return dominos, n

def getSol(n, dominos):
    l = [1] * n
    succ = [n] * n

    pozMax = n - 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if dominos[i][1] == dominos[j][0] and l[j] + 1 > l[i]:
                l[i] = l[j] + 1
                succ[i] = j

        if l[i] > l[pozMax]:
            pozMax = i

    while pozMax < n:
        print(dominos[pozMax])
        pozMax = succ[pozMax]




def mainCode():
    dominos, n = readInput()
    getSol(n, dominos)

mainCode()