#Topological Sort
# topology sort
from queue import Queue

nv, ne = map(int, input().split())

# make refree list and adjacent list
ref = [ 0 ]*nv
adj = [ [] for _ in range(nv+1) ]
for i in range(ne):
    f, s = map(int, input().split())
    adj[f-1].append(s-1)
    ref[s-1] += 1

# Make a queue
Q = Queue()

# Add vertices whose refree count are zero into the queue
for i in range(ne):
    if ref[i] == 0: Q.put(i)

# while Q is not empty
sorted = []
while not Q.empty():
    # Get a vertex from queue
    u = Q.get()
    # Add u into sorted list
    sorted.append(u+1)
    # For all edges those start at vertex u
    for v in adj[u]:
        # decrease refree count of v by 1
        ref[v] -= 1
        # if refree count is 0, add v into the queue
        if ref[v] == 0: Q.put(v)

# print topology sorted list
print(*sorted)