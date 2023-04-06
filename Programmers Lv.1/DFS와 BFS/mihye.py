from collections import deque

n, m, v = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(m)]
graph = []

for _ in range(n + 1):
    graph.append([])

for a, b in list:
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited = [False] * (n + 1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True



dfs(graph,v,visited)
print()
visited = [False] * (n + 1)
bfs(graph,v,visited)


