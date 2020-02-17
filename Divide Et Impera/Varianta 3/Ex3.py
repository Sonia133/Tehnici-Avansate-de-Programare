def readInput():
    v = [int(x) for x in input().split()]

    return v

def getSol(st, dr, v):
    if st == dr:
        return 0
    med = (st + dr) // 2
    s = []
    nrs = getSol(st, med, v)
    nrd = getSol(med + 1, dr, v)
    nrm = 0
    i, j = 0, 0
    a, b = v[st: med + 1], v[med + 1: dr + 1]
    while i < len(a) and j < len(b):
        if a[i] < 2 * b[j]:
            s.append(a[i])
            nrm += j
            i += 1
        else:
            s.append(b[j])
            j += 1

    while i < len(a):
        s.append(a[i])
        nrm += j
        i += 1

    while j < len(b):
        s.append(b[j])
        j += 1

    v[st : dr + 1] = s

    return nrm + nrs + nrd

def mainCode():
    v = readInput()
    nr = getSol(0, len(v) - 1, v)

    print(nr)

mainCode()