# get number of islands
#DFS
def dfs(M, r, c):
    # Mark M[r][c] as visited
    M[r][c] = 0
    adj = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
    for dr, dc in adj:
        # get adjacent coordinate
        nr, nc = r+dr, c+dc
        # boundary check
        if nr < 0 or nr >= len(M) or nc < 0 or nc >= len(M[0]):
            continue
        # visited or sea check
        if M[nr][nc] != 1: continue
        # recursion call for new coordinate
        dfs(M, nr, nc)

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
            dfs(M, i, j)
            for k in M:
              print(*k)

print(islands)