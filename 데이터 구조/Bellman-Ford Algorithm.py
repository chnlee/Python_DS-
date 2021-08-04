# Bellman-Ford Algorithm

Inf = 10**9

nv, ne, sp = map(int, input().split())

E = []
for _ in range(ne):
    v1, v2, w = map(int, input().split())
    E.append((v1-1, v2-1, w))

d = [ Inf ]*nv
d[sp-1] = 0

# relax
for _ in range(nv-1):
    for f, t, w in E:
        if d[f]+w < d[t]: d[t] = d[f]+w
# negative cycle check
isNegCycle = False
for f, t, w in E:
    if d[f]+w < d[t]: isNegCycle = True

if isNegCycle:
    print("NC")
else:
    for i in range(nv):
        print("INF" if d[i] == Inf else d[i])
