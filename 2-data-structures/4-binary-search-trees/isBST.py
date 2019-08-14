# python3
import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**25)

def inorder(index):
  key, left, right = tree[index]

  if left != -1:
    inorder(left)

  result.append(key)

  if right != -1:
    inorder(right)

def is_valid():
  for i in range(len(result) - 1):
    if result[i] >= result[i + 1]:
      return False
  return True

def main():
  for i in range(n):
    tree.append([int(x) for x in input().split()])

  if n == 0:
    print('CORRECT')
  else:
    inorder(0)
    print('CORRECT' if is_valid() else 'INCORRECT')

n = int(input())
tree = []
result = []

threading.Thread(target=main).start()