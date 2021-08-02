# 순열을 위한 재귀함수
def perm(v, r, visit, s):
    if r == 0:
        print(s)
        return
    # v list에 있는 모든 것에 대해서
    for i in range(len(v)):
        # 이미 방문을 했다면 패스
        if visit[i]: continue
        # i번째 원소 방문
        visit[i] = True
        perm(v, r-1, visit, s + (v[i], ))
        visit[i] = False

# 키보드로부터 리스트를 입력받는다
v = input("리스트의 내용 입력 : ").split()
r = int(input("표시할 개수 입력 : "))

visit = [False]*(len(v))

perm(v, r, visit, tuple())

# itertools에 있는 순열 반복함수 permutations 가져오기
from itertools import permutations

# 키보드로부터 리스트를 입력받는다
v = input("리스트의 내용 입력 : ").split()
r = int(input("표시할 개수 입력 : "))

visit = [False]*(len(v))

perm(v, r, visit, tuple())

print("-"*40)
# permutations 반복함수와 for 구문을 이용해서 출력
for k in permutations(v, r):
    print(k)
