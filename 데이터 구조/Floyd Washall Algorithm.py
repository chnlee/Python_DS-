# Floyd Washall Algorithm

Inf = 10**9
n = int(input())
d = [ [Inf]*n for _ in range(n) ]

for i in range(n):
    s = list(map(int, input().split()))
    for j in range(n):
        if s[j] == 1: d[i][j] = 1

# O(V^3)
for k in range(n):
    for u in range(n):
        for v in range(n):
            if d[u][v] > d[u][k] + d[k][v]:
                d[u][v] = d[u][k] + d[k][v]

# Negative Cycle Check
isNegativeCycle = False
for i in range(n):
    if d[i][i] < 0: isNegativeCyclte = True

for i in range(n):
    for j in range(n):
        print(0 if d[i][j] == Inf else 1, end=" ")
    print("")

# Floyd Washall Algorithm

Inf = 10**9
n = int(input())
d = [ ]

for i in range(n):
    s = list(map(int, input().split()))
    d.append(s)

# O(V^3)
for k in range(n):
    for u in range(n):
        for v in range(n):
            if d[u][v] == 1: continue
            if d[u][k] == 1 and d[k][v] == 1:
                d[u][v] = 1

for i in range(n):
    print(*d[i])

