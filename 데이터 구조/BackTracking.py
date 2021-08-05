# sudoku

def solveSudoku(c, space, sudoku):
    if c == len(space):
        return True
    for v in range(1, 10):
        # Horizental check
        isOK = True
        for i in range(9):
            if v == sudoku[space[c][0]][i]:
                isOK = False
                break
        if not isOK: continue
        # Vertical check
        isOK = True
        for i in range(9):
            if v == sudoku[i][space[c][1]]:
                isOK = False
                break
        if not isOK: continue
        sudoku[space[c][0]][space[c][1]] = v
        if solveSudoku(c+1, space, sudoku): return True
    return False

sudoku = []
# 데이터를 입력해야할 위치를 저장하기 위해서 space 정의
space = []
for i in range(9):
    s = list(map(int, input().split()))
    sudoku.append(s)
    for j in range(9):
        if s[j] == 0: space.append((i, j))

solveSudoku(0, space, sudoku)
for i in range(9):
    print(*sudoku[i])

#sudoku using backtracking algorithm

def solveSudoku(c, space, sudoku, hcheck, vcheck, scheck):
    if c == len(space): return True
    row, col = space[c]
    for k in range(1, 10):
        if hcheck[row][k]: continue
        if vcheck[col][k]: continue
        if scheck[(row//3)*3+(col//3)][k]: continue
        sudoku[row][col] = k
        hcheck[row][k] = True
        vcheck[col][k] = True
        scheck[(row//3)*3+(col//3)][k] = True
        if solveSudoku(c+1, space, sudoku, hcheck, vcheck, scheck):
            return True
        hcheck[row][k] = False
        vcheck[col][k] = False
        scheck[(row//3)*3+(col//3)][k] = False
    return False

hcheck = [ [False]*10 for _ in range(9) ]
vcheck = [ [False]*10 for _ in range(9) ]
scheck = [ [False]*10 for _ in range(9) ]
# 데이터를 입력해야할 위치를 저장하기 위해서 space 정의
sudoku = []
space = []
for i in range(9):
    s = list(map(int, input().split()))
    sudoku.append(s)
    for j in range(9):
        if s[j] == 0: space.append((i, j))
        hcheck[i][s[j]] = True
        vcheck[j][s[j]] = True
        scheck[(i//3)*3+(j//3)][s[j]] = True

solveSudoku(0, space, sudoku, hcheck, vcheck, scheck)
for i in range(9):
    print(*sudoku[i])


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
