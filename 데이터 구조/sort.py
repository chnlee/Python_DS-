# #Selection Sort
import time
import random
#Set random seed
random.seed(1000)
def selectionSort(v,a,b):
  for i in range(a,b):
    # 정렬된 부분 
    m = i
    # 정렬안된 부분
    for j in range(i+1,b+1):
      # find min value
      if v[j] < v[m]: m = j
    # change the rightmost value of the sorted list and the smallest value of the unaligned list
    v[i], v[m] = v[m], v[i]
  
n = int(input("n ="))
v = [random.randrange(10**8) for _ in range(n)]
ts = time.time()
selectionSort(v,0,n-1)
et = (time.time()-ts)*1000
print(v[:10])
# {:.1f}는 소수점 첫째자리까지만 나타낸다는 뜻
print(f"Elapes time is {et:.1f}ms.")


#MergeSort
temp = [0]* 10000000
def mergeSort(v,a,b):
  #devide
  c = (a+b)//2
  #conquer
  selectionSort(v,a,c)
  selectionSort(v,c+1,b)
  # merge values which were devided
  # i means the first value of the first list
  # j means the first value of the second list
  # k means the fisrt value of the merged list 
  i,j,k = a,c+1,0
  while i<=c and j<=b:
    # 값이 v[i]가 더 큰 경우
    if v[i] <= v[j]:
      temp[k] = v[i]
      #다음 element로 이동
      k, i = k+1, i+1
    # 값이 v[j]]가 더 큰 경우
    else: 
      temp[k] = v[j]
      k, j = k+1, j+1
  #자투리 값 제거
  while i<=c:
    temp[k] = v[i]
    k, i = k+1, i+1
  while j<=b:
    temp[k] = v[j]
    k, j = k+1, j+1
  #temp에 할당된 값을 다시 리스트에 계속 넣는다. = 합병완료  
  for i in range(k):
    v[a+i] = temp[i]

n = int(input("n ="))
v = [random.randrange(10**8) for _ in range(n)]
ts = time.time()
mergeSort(v,0,n-1)
et = (time.time()-ts)*1000
print(v[:10])
# {:.1f}는 소수점 첫째자리까지만 나타낸다는 뜻
print(f"Elapes time is {et:.1f}ms.")

#MergeSort using recursive function
temp = [0]* 10000000
def mergeSort(v,a,b):
  if a==b:return
  #devide
  c = (a+b)//2
  #conquer
  print("a")
  mergeSort(v,a,c)
  print("b")
  mergeSort(v,c+1,b)
  print("c")
  # merge values which were devided
  # i means the first value of the first list
  # j means the first value of the second list
  # k means the fisrt value of the merged list 
  i,j,k = a,c+1,0
  while i<=c and j<=b:
    # 값이 v[i]가 더 큰 경우
    if v[i] <= v[j]:
      temp[k] = v[i]
      #다음 element로 이동
      k, i = k+1, i+1
    # 값이 v[j]]가 더 큰 경우
    else: 
      temp[k] = v[j]
      k, j = k+1, j+1
  #자투리 값 제거
  while i<=c:
    temp[k] = v[i]
    k, i = k+1, i+1
  while j<=b:
    temp[k] = v[j]
    k, j = k+1, j+1
  #temp에 할당된 값을 다시 리스트에 계속 넣는다. = 합병완료  
  for i in range(k):
    v[a+i] = temp[i]

n = int(input("n ="))
v = [random.randrange(10**8) for _ in range(n)]
ts = time.time()
mergeSort(v,0,n-1)
et = (time.time()-ts)*1000
print(v[:10])
# {:.1f}는 소수점 첫째자리까지만 나타낸다는 뜻
print(f"Elapes time is {et:.1f}ms.")




import random
import time

# Set random seed
random.seed(1000)

# partition
# return index of pivot
def partition(v, a, b):
    pivot, i, j = v[b], a, b-1
    while i <= j:
        if v[i] <= pivot: i += 1
        else:
            v[i], v[j] = v[j], v[i]
            j -= 1
    v[i], v[b] = v[b], v[i]
    return i #pivot의 순서

 

# Quick Sort
def quickSort(v, a, b):
    if a >= b: return
    c = partition(v, a, b)
    quickSort(v, a, c-1)
    quickSort(v, c+1, b)
 
n = int(input("n = "))
v = [random.randrange(10**8) for _ in range(n)]
ts = time.time()
quickSort(v, 0, n-1)
et = (time.time() - ts)*1000

print(v[:10])
print(f"Elapsed time is {et:.1f}ms.")

#N,K 랜덤 생성

def kthElement(v,k):
  return kthElementInt(v,k-1,0,len(v)-1)

def kthElementInt(v,k,a,b):
  c = partition(v,a,b)
  if c==k: return print(v[c])
  if k<c: return kthElementInt(v,k,a,c-1)
  return kthElementInt(v,k,c+1,b)

n = int(input("n = "))
v = [random.randrange(10**8) for _ in range(n)]
k = int(input("k = "))
kthElement(v,k)

