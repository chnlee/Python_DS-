# count GCD(n, i) = 1 for 1 .. n
import time

# Euculid Induction Algorithm
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

# Euler's totient
def phi1(n):
    cnt = 0
    for i in range(1, n+1):
        if gcd(n, i) == 1: cnt += 1
    return cnt

def phi2(n):
    et = 1
    if n%2 == 0:
        n //= 2
        while n%2 == 0:
            et *= 2
            n //= 2
    p = 3
    while p*p <= n:
        if n%p == 0:
            n //= p
            et *= p-1
            while n%p == 0:
                et *= p
                n //= p
        p += 2
    if n != 1: et *= n-1
    return et

n = int(input("n = "))
ts = time.time()
cnt = phi2(n)
et = (time.time() - ts)*1000
print(cnt)
print("Elapsed time is %.1fms."%et)
