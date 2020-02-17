class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def readInput():
    inO = [int(x) for x in input().split()]
    postO = [int(x) for x in input().split()]

    return inO, postO, len(inO)

def preOrder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node.data, end=' ')
    inOrder(node.right)

def postOrder(node):
    if node == None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=' ')

def buildTree(inO, postO, inordInd, index, l, r, cnt):
    if l > r:
        return None
    node = Node(postO[index[0]])
    index[0] -= 1
    cnt[0] += 1
    if l == r:
        return node
    direction = int(inordInd[node.data])
    node.right = buildTree(inO, postO, inordInd, index, direction + 1, r, cnt)
    node.left = buildTree(inO, postO, inordInd, index, l, direction - 1, cnt)

    return node

def mainCode():
    inO, postO, n = readInput()
    inordInd = [None] * (n + 1)
    for i in range(n):
        inordInd[inO[i]] = i
    cnt = [0]
    index = [n - 1]
    root = buildTree(inO, postO, inordInd, index, 0, n - 1, cnt)
    if cnt[0] == n:
        preOrder(root)
    else:
        print('-1')


mainCode()