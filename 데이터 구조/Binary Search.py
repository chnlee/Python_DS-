# Entrance Check
from queue import Queue, PriorityQueue

n = int(input())
wtm = list(map(int, input().split()))

# 현재 작업을 하지 않는 심사관들
pool = Queue()
for i in range(len(wtm)): pool.put(i)
# 현재 작업중인 심사관들
work = PriorityQueue()
# 현재 시간
tm = 0
# 대기하고 있는 사람들이 있고, 심사하는 심사관이 존재하는 경우
while n > 0 or not work.empty():
    # 대기하고 있는 사람들이 있고, 심사하지 않는 심사관이 있는경우
    while n > 0 and not pool.empty():
        u = pool.get()
        work.put((tm+wtm[u], u))
        n -= 1
        print(f"{tm:3} IN : {u}")
    tm, u = work.get()
    pool.put(u)
    print(f"{tm:3} OUT : {u}")

print(tm)

#이분탐색 이용한 Entrance check
def checkPass(wtm, n, tm):
    sum = 0
    for k in wtm:
        sum += tm//k
    return n <= sum

n = int(input())
wtm = list(map(int, input().split()))
mintm = 10**9
for k in wtm: mintm = min(mintm, k)

# mintm-1 : always fail because fastest officer cannot 1 person
# mintm*n : always pass because all persons are served fastest officer
left, right = mintm-1, mintm*n
# left와 right가 서로 이웃하고 있지 않는 한
while left+1 < right:
    c = (left+right)//2
    #이분탐색을 할 때 pass and fail로 찾는 경우
    print(f"{c} : {'pass' if checkPass(wtm, n, c) else 'fail'}")
    if checkPass(wtm, n, c): right = c
    else: left = c
print(right)
