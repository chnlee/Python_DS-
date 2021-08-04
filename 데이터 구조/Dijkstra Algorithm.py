# Dijkstra Algorithm
from queue import PriorityQueue

Inf = 10**9

nv, ne, sp = map(int, input().split())
# 인접리스트를 작성합니다.
adj = [ [] for _ in range(nv) ]
# 간선의 개수만큼 읽어서 adj 자료구조 완성
for i in range(ne):
    v1, v2, w = map(int, input().split())
    # convert undirected graph to directed graph
    adj[v1-1].append((v2-1, w))

# Make vertex values and visited flags
d = [Inf]*nv
visit = [False]*nv

# Make a priority Queue
pq = PriorityQueue()

# set d[sp] as 0 and add (0, sp) into priority queue
d[sp-1] = 0
pq.put((0, sp-1))

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
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            pq.put((d[v], v))

for i in range(nv):
    print("INF" if d[i] == Inf else d[i])