# import numpy as np

# v = np.array(range(1,10))
# print(v)
# w = np.arange(1,10)
# print(w)
# vl = [1,2,3.5,4]
# np.array(vl)
# #문자열로 변경됨
# vl = [1,3,"abc",4]
# np.array(vl)

# vl = [ 1, 3, [1,2],4]
# np.array(vl)

import numpy as np
#배열은 바로 연산 가능
x = np.arange(0,100)
y = x**2 +3

print(y)
#반복문 연산 <- 속도가 느리다.
lx = list(range(0,100))
ly = [ x**2 + 3 for x in lx]
print(ly)
#numpy 다차원 배열
M =np.array([[1,2,3],[4,5,6]])
#형태를 변경할 수 있음 3*2로 변경
M = M.reshape(3,2)
print(M)

#numpy 인덱싱과 자르기
xl = np.array((-4,10,2,6,-3,7))
xl[xl<0] = 0
print(xl)
#0보다 작은 값에 대한 true false 적용
t = xl < 0
print(t)
# 적용된 true false 값에 대해 -1값 적용
xl[t] = -1
print(xl)

#브로드캐스팅 : 각각의 element 연산
#shape : 길이와 같은 

a = np.arange(1,11,2)
b = np.arange(2,11,2)
#사칙연산 다 가능
print(a+b)

#조건부 함수 이해하기
a = np.arange(10)
print(np.where(a<5,a,10*a))

