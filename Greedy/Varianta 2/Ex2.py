def readInput():
    n = (int(input()))
    texts = []
    for i in range(n):
        texts.append([int(x) for x in input().split()])

    return n, texts

def getSol(texts):
    val = 0
    sum = 0
    for x in texts:
        sum += x[0]
        val += x[1] * sum

    return val

def driveCode():
    n, texts = readInput()
    texts = sorted(texts, key = lambda x: x[1], reverse = True)
    val = getSol(texts)

    for i in range(n):
        print(str(i + 1) + ':', end = ' ')
        print(texts[i])

    print(val)


driveCode()