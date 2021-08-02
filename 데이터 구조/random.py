# import random
# #랜덤의 시퀀스 고정= 항상 같은 난수 시퀀스 발생
# random.seed(100)

# x = [ random.randrange(1,101) for _ in range(10)]

# print(*x)

import random

n = int(input("n = "))

inCount = 0

for i in range(n):
  # random으로 [0,1] 사이의 값으로 x,y
  x = random.randrange(10**8)/10**8
  y = random.randrange(10**8)/10**8
  # x^2 + y^2 값이 1이하면 안에 있는 점 개수 추가
  if x**2 + y**2 <=1: inCount +=1


print(f"pi = {4*inCount/n:.4f}")

#inCount : n =  4분원의 면적 : 1(정사각형의 면적)
#.4f : 소수점 4개 이하


