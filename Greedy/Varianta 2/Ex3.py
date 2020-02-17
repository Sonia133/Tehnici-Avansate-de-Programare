import heapq as hq

def findParent(node, parent) :
    if parent[node] == node:
        return node
    else:
        return findParent(parent[node], parent)

def readInput():
    n = int(input())
    actv = []
    maxdl = 0

    for i in range(n):
        p, d = [int(x) for x in input().split()]
        hq.heappush(actv, (-p,(d,i+1)))
        if maxdl < d:
            maxdl = d
    return actv, maxdl

def driveCode() :
    actv, maxdl = readInput()
    parent = [i for i in range(maxdl + 1)]
    sum = 0

    while actv:
        index = findParent(actv[0][1][0], parent)
        if index > 0:
            sum += actv[0][0]
            print(actv[0][1][1], end = ' ')
            parent[index] = findParent(index - 1, parent)
        hq.heappop(actv)

    print()
    print(-sum)

driveCode()