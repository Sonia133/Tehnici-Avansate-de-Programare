def readInput():
    n = int(input())
    intervals = [None] * n
    for i in range(n):
        intervals[i] = [int(x) for x in input().split()]
        intervals[i].append(0)
    return n, intervals

def getSol(n, intervals, sol):
    left = n
    cnt = 0
    i = 0
    j = 1
    ok = 0

    while left > 0:
        if ok == 0:
            if intervals[i][2] == 1:
                i += 1
            else:
                if sol[0][0] == -1:
                    sol[0][0] = intervals[i]
                    intervals[i][2] = 1
                    left -= 1
                else:
                    cnt += 1
                    sol.append([intervals[i]])
                    left -= 1
                    intervals[i][2] = 1
                    j = i + 1
                ok = 1
        if ok == 1:
            if intervals[j][0] >= intervals[i][1] and intervals[j][2] == 0:
                sol[cnt].append(intervals[j])
                left -= 1
                intervals[j][2] = 1
                i = j
                if i == n - 1:
                    i = 0
                    j = 1
                    ok = 0
                else:
                    j += 1
            else:
                j += 1
                if j == n:
                    i = 0
                    j = 1
                    ok = 0

    return cnt, sol


def mainCode():
    n, intervals = readInput()
    sol = [[-1]]
    intervals = sorted(intervals, key = lambda x: (x[1], x[0]))
    count, sol = getSol(n, intervals, sol)

    print(count)
    for x in sol:
        print(x)


mainCode()