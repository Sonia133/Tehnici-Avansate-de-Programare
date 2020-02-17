def readInput() :
    n = int(input())
    intervals = [None] * n
    for i in range(n):
        intervals[i] = [int(x) for x in input().split()]
    return n, intervals

def getSol(n, intervals, sol):
    count = 0
    index = -1
    maxF = -1

    for x in intervals:
        if sol[0][0] == -1:
            sol[0][0] = x
            count += 1
        else:
            appended = 0
            maxF = -1
            index = -1
            for i in range(len(sol)):
                if sol[i][len(sol[i]) - 1][1] <= x[0]:
                    if sol[i][len(sol[i]) - 1][1] > maxF:
                        maxF = sol[i][len(sol[i]) - 1][1]
                        index = i
                    appended = 1
            if appended == 0:
                count += 1
                sol.append([x])
            else:
                sol[index].append(x)

    return count, sol

def mainCode():
    n, intervals = readInput()
    sol = [[-1]]
    print(intervals)
    intervals = sorted(intervals, key = lambda x: (x[1], x[0]))
    count, sol = getSol(n, intervals, sol)

    print(count)
    for x in sol:
        print(x)


mainCode()