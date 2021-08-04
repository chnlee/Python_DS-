# MST with Prim Algorithm
# Prim 알고리즘을 사용할 때, heapq 사용
from heapq import *

Inf = 10**9

nv, ne = map(int, input().split())
# 인접리스트를 작성합니다.
adj = [ [] for _ in range(nv+1) ]
# 간선의 개수만큼 읽어서 adj 자료구조 완성
for i in range(ne):
    v1, v2, w = map(int, input().split())
    # convert undirected graph to directed graph
    adj[v1].append((v2, w))
    adj[v2].append((v1, w))
print(adj)
# Make vertex values and visited flags
d = [Inf]*(nv+1)
visit = [False]*(nv+1)

# Make a priority Queue
pq = []

# Make vertex 1 as a starting point
d[1] = 0
pq.append((0, 1))

# while priority queue is not empty
while len(pq) > 0:
    # get first item from priority queue
    _, u = heappop(pq)
    # if vertex u is already visited, do nothing.
    if visit[u]: continue
    # Mark vertex u as visited
    visit[u] = True
    # for all edges whose are starting at vertex u
    for v, w in adj[u]:
        # if vertex v is already visited, do nothing.
        if visit[v]: continue
        # if vertex v's value is greater than edge's weight
        if d[v] > w:
            d[v] = w
            heappush(pq, (w, v))

sum = 0
for i in range(1, nv+1): sum += d[i]
print(sum)


# MST with Prim Algorithm
# Prim 알고리즘을 사용할 때, PriorityQueue 사용
from queue import PriorityQueue

Inf = 10**9

nv, ne = map(int, input().split())
# 인접리스트를 작성합니다.
adj = [ [] for _ in range(nv+1) ]
# 간선의 개수만큼 읽어서 adj 자료구조 완성
for i in range(ne):
    v1, v2, w = map(int, input().split())
    # convert undirected graph to directed graph
    adj[v1].append((v2, w))
    adj[v2].append((v1, w))

# Make vertex values and visited flags
d = [Inf]*(nv+1)
visit = [False]*(nv+1)

# Make a priority Queue
pq = PriorityQueue()

# Make vertex 1 as a starting point
d[1] = 0
pq.put((0, 1))

# while priority queue is not empty
while not pq.empty():
    # get first item from priority queue
    _, u = pq.get()
    # if vertex u is already visited, do nothing.
    if visit[u]: continue
    # Mark vertex u as visited
    visit[u] = True
    # for all edges whose are starting at vertex u
    for v, w in adj[u]:
        # if vertex v is already visited, do nothing.
        if visit[v]: continue
        # if vertex v's value is greater than edge's weight
        if d[v] > w:
            d[v] = w
            pq.put((w, v))

sum = 0
for i in range(1, nv+1): sum += d[i]
print(sum)
