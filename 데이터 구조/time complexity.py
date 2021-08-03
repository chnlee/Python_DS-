# # import random
# # import time

# # n = int(input("n = "))

# # random.seed(1000)
# # v = [ random.randrange(10**8) for _ in range(n)]
# # # x in v라는 함수의 영향이 커지지 않았음
# # v = set(v)
# # ts = time.time()
# # count = 0
# # for _ in range(1000):
# #   x = random.randrange(10**8)
# #   if x in v : count +=1
# # et = (time.time()-ts)*1000

# # print(count)

# # print(f"Elapsed time is {et:.1f}ms.")


# # #O(N)
# # import random
# # import time

# # n = int(input("n = "))

# # random.seed(1000)


# # count = 0
# # for i in range(1, n+1):
# #   if i % 2 ==0 : count +=1
# # et = (time.time()-ts)*1000

# # print(count)

# # print(f"Elapsed time is {et:.1f}ms.")

# # #O(n^2*k)
# # import random
# # import time

# # n,k = map(int, input("n, k = ").split())

# # ts = time.time()
# # v = [i for i in range(n)]
# # r = []
# # while len(v) > 0:
# #   for _ in range(k-1):
# #     v.append(v.pop(0))
# #   r.append(v.pop(0))
# # et = (time.time()-ts)*1000

# # print(r[:10])

# # print(f"Elapsed time is {et:.1f}ms.")


# #O(nk) - queue 사용
# import random
# import time
# from queue import Queue
# n,k = map(int, input("n, k = ").split())

# ts = time.time()
# v = Queue()
# for i in range(n): v.put(i)
# r = []
# while v.qsize() > 0:
#   for _ in range(k-1):
#     v.put(v.get())
#   r.append(v.get())
# et = (time.time()-ts)*1000

# print(r[:10])

# print(f"Elapsed time is {et:.1f}ms.")

count = 0

def fast(n):
  global count
  count += 1
  if n <=1 : return 0
  return fast(n//2) + 1

n = int(input("n="))

print(fast(n))

print("count = %d"%count)