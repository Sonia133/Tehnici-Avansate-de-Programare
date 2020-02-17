from heapq import merge

def readInput():
    first = [int(x) for x in input().split()]
    second = [int(x) for x in input().split()]

    return first, second, len(first), len(second)

def getSol(first, second, n, m):
    i, j, median = 0, 0, 0
    minIndex, maxIndex = 0, n
    while minIndex <= maxIndex:
        i = (minIndex + maxIndex) // 2
        j = (n + m + 1) // 2 - i

        if i == 0:
            median = second[j - 1]
        elif j == 0:
            median = first[i - 1]
        else:
            if i > 0 and j < n and second[j - 1] > first[i]:
                minIndex = i + 1
            elif i > 0 and j < n and first[i - 1] > second[j]:
                maxIndex = i - 1

            else:
                median = max(first[i - 1], second[j - 1])
                break

    if (n + m) % 2 == 1:
        return median

    if i == n:
        return (median + second[j]) // 2

    if j == m:
        return (median + first[i]) // 2

    return (median + min(first[i], second[j])) // 2

def mainCode():
    first, second, n, m = readInput()
    if n < m:
        median = getSol(first, second, n, m)
    else:
        median = getSol(second, first, m, n)

    print(median)


mainCode()