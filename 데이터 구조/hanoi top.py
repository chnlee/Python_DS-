#stack using list

stack = []
#모두 O(1)
# push : stack.append(<new item>)
# pop : stack.pop()
# top : stack[-1]
# empty : len(stack) == 0
# size : len(stack)


def push(stack, x):
  stack.append(x)

def pop(stack):
  return stack.pop()
  
def top(stack):
  return stack[-1]
  
def empty(stack):
  return len(stack) == 0
  
def size(stack):
  return len(stack)


peg = [ k for  k in range(31,0,-1)]

print(peg)

def ruler(n):
    if n%2 == 1: return 1
    return 1+ruler(n//2)

k = int(input("k = "))
print(ruler(k))

for i in range(100):
    if k & (2**i):
        print(i+1)
        break

