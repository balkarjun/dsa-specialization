# python3
import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**25)

def inorder(index, tp):
  key, left, right = tree[index]

  if left != -1:
    tp = 'root'
    inorder(left, 'left')
  
  if len(result) > 0:
    if result[-1][0] > key:
      falses.append(False)
    elif result[-1][0] == key and (result[-1][1] != 'root' and tp != 'right'):
      falses.append(False)

  result.append([key, tp])

  if right != -1:
    result[-1][1] = 'root'
    inorder(right, 'right')

def main():
  for i in range(n):
    tree.append([int(x) for x in input().split()])
  
  if n == 0:
    print('CORRECT')
  else:
    inorder(0, 'root')
    if len(falses) == 0:
      print('CORRECT')
    else:
      print('INCORRECT')

n = int(input())
tree = []
result = []
falses = []

threading.Thread(target=main).start()