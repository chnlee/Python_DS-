from bisect import *

v = list(map(int,input().split()))
v.sort()
n = int(input())
for _ in range(n):
  k = int(input())
  idx1 = bisect_left(v,k) - 1
  idx2 = bisect_right(v,k)
  if idx1 < 0 and idx2>=len(v) : print("None None")
  elif idx1 < 0:
    print("None %d"%v[idx2])
  elif idx2 >=len(v): print("%d None"%(v[idx1]))
  else: 
    print("{0} {1}".format(v[idx1], v[idx2]))