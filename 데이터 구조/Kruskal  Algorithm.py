# MST with Kruskal algorithm
#disjoint set
def getRoot(djs, x):
    if djs[x] == x: return x
    djs[x] = getRoot(djs, djs[x])
    return djs[x]

nv, ne = map(int, input().split())
# Make edge list
E = []
for _ in range(ne):
    v1, v2, w = map(int, input().split())
    E.append((w, v1-1, v2-1))
# sort edge list
E.sort()

# Make vertices disjoint sets.
djset = [ i for i in range(ne) ]

MST = 0
for w, v1, v2 in E:
    # get disjoint set's roots of v1 and v2
    r1 = getRoot(djset, v1)
    r2 = getRoot(djset, v2)
    # if two roots are same, do nothing
    if r1 == r2: continue
    # Add this weight to MST
    MST += w
    # Union r1 set adn r2 set
    djset[r2] = r1

print(MST)