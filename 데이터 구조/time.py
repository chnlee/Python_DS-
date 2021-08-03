import random
import time

n = int(input("n = "))

random.seed(1000)
v = [ random.randrange(10**8) for _ in range(n)]
# x in v라는 함수의 영향이 커지지 않았음
v = set(v)
ts = time.time()
count = 0
for _ in range(1000):
  x = random.randrange(10**8)
  if x in v : count +=1
et = (time.time()-ts)*1000

print(count)

print(f"Elapsed time is {et:.1f}ms.")