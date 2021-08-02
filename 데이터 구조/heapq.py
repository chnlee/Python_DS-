from heapq import *
import random

random.seed(100) #시드값 설정, 같은 시퀀스 발생
h = [random.randrange(10**8) for _ in range(10**6)]
#heapq보다 시간단축
h.sort()
print(h[:10])
#list를 힙 구조로 생성함
heapify(h)
#heap에서 가장 작은 아이템 가져오기 + 삭제
sorted = [heappop(h) for _ in range(len(h))]

print(sorted[:10])

#가장 작은 절대값 출력하기

from heapq import *

heap = []
n =int(input())
for i in range(n):
  k = int(input())
  if k == 0:
    x = heappop(heap)
    print((x+1)//-2 if x%2 == 1 else x//2)
  else:
    heappush(heap,-2*k-1 if k<0 else 2*k)