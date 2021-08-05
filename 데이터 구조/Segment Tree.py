# get minimum values for multiple areas
from random import randrange, seed
import time

seed(1000)
v = [ randrange(10**8) for _ in range(10**6) ]
m = []
for _ in range(200):
    a = randrange(10**6)
    b = randrange(10**6)
    m.append((min(a, b), max(a, b)))

ts = time.time()
for a, b in m:
    vmin = v[a]
    for i in range(a+1, b+1):
        if v[i] < vmin: vmin = v[i]
    print(vmin)
et = (time.time() - ts)*1000
print("Elpase time is %.1fms"%et)

# get minimum values for multiple areas
from random import randrange, seed
import time

def initSeg(st, r, v, a, b):
    if a == b:
        st[r] = v[a]
        return st[r]
    c = (a+b)//2
    st[r] = min(initSeg(st, r*2, v, a, c), 
        initSeg(st, r*2+1, v, c+1, b))
    return st[r]

def getSeg(st, r, a, b, ra, rb):
    if rb < a or b < ra: return 10**8
    if ra <= a and b <= rb: return st[r]
    c = (a+b)//2
    return min(getSeg(st, r*2, a, c, ra, rb),
        getSeg(st, r*2+1, c+1, b, ra, rb))

seed(1000)
v = [ randrange(10**8) for _ in range(10**6) ]
m = []
for _ in range(200):
    a = randrange(10**6)
    b = randrange(10**6)
    m.append((min(a, b), max(a, b)))

ts = time.time()
st = [ 0 ]*(len(v)*4)
initSeg(st, 1, v, 0, len(v)-1)
for a, b in m:
    #vmin = v[a]
    #for i in range(a+1, b+1):
    #   if v[i] < vmin: vmin = v[i]
    vmin = getSeg(st, 1, 0, len(v)-1, a, b)
    print(vmin)
et = (time.time() - ts)*1000
print("Elpase time is %.1fms"%et)