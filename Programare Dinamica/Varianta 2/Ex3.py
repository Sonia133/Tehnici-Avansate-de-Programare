def readInput():
    n = int(input())
    dict = [None] * (n + 2)

    for i in range(2, n + 2):
        dict[i] = input()

    word = input()

    dict[0] = '0'
    dict[1] = '1'

    return dict, word

def getSol(word, dict, n):
    L = [-1] * n
    prev = [-1] * n
    L[0] = 0

    for i in range(1, n):
        for j in range(i, 0, -1):
            if word[j : i + 1] in dict:
                if (L[j - 1] + 1 < L[i] or L[i] == -1) and L[j - 1] != -1 :
                    L[i] = L[j - 1] + 1
                    prev[i] = j - 1

    return prev, L[n - 1]

def printStr(prev, i, word):
    if prev[i] > 0 :
        printStr(prev, prev[i], word)

    print(word[prev[i] + 1 : i + 1], end = ' ')

def mainCode():
    dict, word = readInput()
    prev, cnt = getSol(word, dict, len(word))
    print(cnt)
    printStr(prev, len(word) - 1, word)

mainCode()