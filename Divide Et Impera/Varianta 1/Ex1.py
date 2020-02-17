class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def readInput():
    arr = [x for x in input().split()]
    tree = [None] * len(arr)
    for i in range(len(arr)):
        if arr[i] != 'null' :
            tree[i] = int(arr[i])
        else:
            tree[i] = -1

    return tree

cnt = 0

def createTree(tree):
    global cnt
    if len(tree) == 0:
        return 0
    if tree[cnt] != -1:
        node = Node(tree[cnt])
    else:
        node = None
    if cnt == len(tree) - 1:
        return node
    cnt += 1
    if node != None:
        node.left = createTree(tree)
        node.right = createTree(tree)

    return node

def preOrder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preOrder(node.left)
    preOrder(node.right)

def verifyTree(node, minData, maxData):
    if node == None:
        return 1
    if minData > node.data or node.data > maxData:
        return 0
    return (verifyTree(node.left, minData, node.data - 1) and
            verifyTree(node.right, node.data + 1, maxData))


def mainCode():
    tree = readInput()
    root = createTree(tree)
    minData = -200
    maxData = 200
    isBst = verifyTree(root, minData, maxData)

    if isBst:
        print ('Yes')
    else:
        print('No')

mainCode()