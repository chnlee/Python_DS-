# q = []
# q.append(10)
# q.append(20)
# q.append(30)
# #성능이슈 시간복잡도 O(N)
# print(q.pop(0))
# print(q.pop(0))

# import queue

# Q = queue.Queue()

# Q.put(10)
# Q.put(20)
# print(Q.get())
# Q.put(30)
# print(Q.get())
# print(Q.get())

#주차장

from queue import Queue 
from heapq import *

#parking lot number and incomming cars number
n,k = map(int, input().split())
# 현재 비어있는 주차공간
ep = Queue() #empty park
for i in range(n):
  ep.put(i+1)
# 주차된 차에 대한 스케쥴
ps = []

# for loop 
for _ in range(k):
  # arrival time and depart time
  arr, dep = map(int, input().split())
  # remove from ps(parking schedule)
  while len(ps) > 0 and ps[0][0] <= arr:
    u = heappop(ps)
    ep.put(u[1])
  # if there is not any free parking lot.
  if ep.empty(): print(0)
  else: 
    u = ep.get()
    heappush(ps, (dep, u))
    print(u)
