import time
import math

def fib(n):

    if n == 0: return 0

    if n == 1: return 1

    return fib(n-1)+fib(n-2)

 

# forward programming

def fib1(n):

    f = [0, 1]

    for i in range(2, n+1, 2):

        f[0] += f[1]

        f[1] += f[0]

    return f[n%2]

 

# dynamic programming

def fib2(dp, n):

    if n <= 1: return n

    if dp[n] != None: return dp[n]

    dp[n] = fib2(dp, n-1) + fib2(dp, n-2)

    return dp[n]

 

n = int(input("n = "))

ts = time.time()

print(f"fib({n}) = {fib1(n)}")

dp = [None]*(n+1)

print(f"fib({n}) = {fib2(dp, n)}")

et = (time.time() - ts)*1000

print("Elapsed time is %.1fms"%et)

#mathmetics method
def fib3(n):
  phi = 1.618034
  return int((phi**n-(1-phi)**n)/math.sqrt(5))
#matrix
def mul(a, b):
    m11, m12 = a[0]*b[0] + a[1]*b[2], a[0]*b[1] + a[1]*b[3]
    m21, m22 = a[2]*b[0] + a[3]*b[2], a[2]*b[1] + a[3]*b[3]
    return (m11, m12, m21, m22)

def fib4(n):
    a, b = (1, 1, 1, 0), (1, 0, 0, 1)
    while n > 0:
        if n%2 == 1: b = mul(a, b)
        a = mul(a, a)
        n //= 2
    return b[2]

n = int(input("n = "))
print(fib(n))

# 타일링
n = int(input("n = "))
f = (1, -1)
print((2**(n+1) + f[n%2])//3)


#k금액을 만드는 최소 동전의 개수 구하기
def coincount(dp, coins, k):
    if k < 0: return 10**9
    if k == 0: return 0
    if dp[k] != None: return dp[k]

    minv = 10**9
    for c in coins:
        minv = min(minv, coincount(dp, coins, k-c))
    dp[k] =  minv+1
    return dp[k]

 
v = list(map(int, input().split()))
k = int(input())
dp = [None]*(k+1)
r = coincount(dp, v, k)
print(r if r < 10**9 else "Cannot")