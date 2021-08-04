#BFS
from queue import Queue


def bfs(M, r, c):
    # Make a queue named Q
    Q = Queue()
    # add start point to Q
    Q.put((r, c))
    # Mark start point as visited
    M[r][c] = 2
    # while Q is not empty
    while not Q.empty():
        # get a first item of queue
        r, c = Q.get()
        adj = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for dr, dc in adj:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= len(M): continue
            if nc < 0 or nc >= len(M[0]): continue
            if M[nr][nc] != 1: continue
            M[nr][nc] = 2
            Q.put((nr, nc))

n, m = map(int, input().split())
M = []
for i in range(n):
    line = input()
    s = []
    for k in line:
        s.append(1 if k=='1' else 0)
    M.append(s)

islands = 0
for i in range(n):
    for j in range(m):
        if M[i][j] == 1:
            islands += 1
            bfs(M, i, j)

print(islands)

#다른 방법
# get number of islands
from queue import Queue

def bfs(M, r, c):
    # Make a queue named Q
    Q = Queue()
    # add start point to Q
    Q.put((r, c))
    # while Q is not empty
    while not Q.empty():
        # get a first item of queue
        r, c = Q.get()
        if M[r][c] != 1: continue
        M[r][c] = 2
        adj = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for dr, dc in adj:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= len(M): continue
            if nc < 0 or nc >= len(M[0]): continue
            if M[nr][nc] != 1: continue
            Q.put((nr, nc))

n, m = map(int, input().split())
M = []
for i in range(n):
    line = input()
    s = []
    for k in line:
        s.append(1 if k=='1' else 0)
    M.append(s)

islands = 0
for i in range(n):
    for j in range(m):
        if M[i][j] == 1:
            islands += 1
            bfs(M, i, j)

print(islands)
