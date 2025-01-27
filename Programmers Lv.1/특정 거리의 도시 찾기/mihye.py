import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n, m, k, x = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)
check = False

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append(b)


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드를 확인
        for i in graph[now]:
            cost = dist + 1
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


# 다익스트라 알고리즘을 수행
dijkstra(x)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
