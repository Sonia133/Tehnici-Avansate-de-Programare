def readInput():
    n = int(input())
    arr = [int(x) for x in input().split()]

    return n, arr

def getSol(arr, l, r):
    if l == r:
        return arr[l]

    if l + 1 == r and arr[l] >= arr[r]:
        return arr[l]

    if l + 1 == r and arr[l] < arr[r]:
        return arr[r]

    mid = (l + r) // 2
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return arr[mid]

    if arr[mid] < arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return getSol(arr,mid + 1, r)

    if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
        return getSol(arr, l, mid - 1)


def mainCode():
    n, arr = readInput()
    sol = getSol(arr, 0, n)

    print(sol)

mainCode()