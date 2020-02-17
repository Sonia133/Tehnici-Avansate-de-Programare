def readInput():
    n = int(input())
    v = [int(x) for x in input().split()]

    return n, v

def getSol(st, dr, arr):
    if st == dr:
        if arr[st] == st:
            return st
        else:
            return -1

    med = (st + dr) // 2
    if arr[med] == med:
        return med
    if arr[med] < med:
        return getSol(med + 1, dr, arr)
    if arr[med] > med:
        return getSol(st, med - 1, arr)


def mainCode():
    n, v = readInput()
    ok = getSol(0, n - 1, v)

    if ok == -1:
        print('no')
    else:
        print(ok)


mainCode()