n, m = [int(i) for i in input().split()]
viz = [0] * (n + 1)
level = [0] * (n + 1)
parent = [0] * (n + 1)
friends = [[]] * (n + 1)

def dfs(node):
    viz[node] = 1
    for x in friends[node]:
        if viz[x] == 0:
            dfs(x)

    if level[node] == 0:
        print(node, end =' ')
        level[parent[node]] = 1


def mainCode():
    for i in range(m):
        a, b = [int(i) for i in input().split()]
        parent[b] = a
        friends[a].append(b)
        friends[b].append(a)

    dfs(1)

mainCode()
