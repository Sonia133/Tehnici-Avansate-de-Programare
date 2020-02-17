def readInput() :
    n = int(input())
    arr = [int(x) for x in input().split()]

    return arr, n

def getSol(n, arr, stacks) :
    for i in range(n):
        if stacks[0][0] == -1:
            stacks[0][0] = arr[i]
        else:
            appended = 0
            for curr in stacks:
                if arr[i] < curr[len(curr) - 1]:
                    curr.append(arr[i])
                    appended = 1
                    break
            if appended == 0:
                stacks.append([arr[i]])

    return stacks

def driveCode() :
    arr, n = readInput()
    stacks = [[-1]]
    stacks = getSol(n, arr, stacks)

    for x in stacks:
        print(x)

driveCode()