def readInput() :
    n = int(input())
    activ = [None] * n
    for i in range(n):
        activ[i] = ([int(x) for x in input().split()])
        activ[i].append(i + 1)
    return n, activ

def getSol(n, activ, activSorted) :
    currTime = 0
    sol = [None] * n
    delay = 0

    for i in range(n):
        sol[i] = ([currTime, currTime + activSorted[i][0]])
        currTime += activSorted[i][0]
        sol[i].append(currTime - activSorted[i][1])
        delay = max(delay , currTime - activSorted[i][1])

    return delay, sol

def driveCode() :
    n, activ = readInput()
    activSorted = sorted(activ, key = lambda x : x[1])
    delay, sol = getSol(n, activ, activSorted)

 

    print('Propunere:')
    for i in range(n):
        print(str(activSorted[i][2]) + ':', end = ' ')
        print(sol[i])
    print('Intarziere', end = ' ')
    print(delay)

driveCode()