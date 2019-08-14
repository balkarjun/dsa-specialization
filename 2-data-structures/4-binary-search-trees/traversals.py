# python3
import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**25)

def inorder(index):
  # left -> root -> right
  key, left, right = tree[index]

  if left != -1:
    inorder(left)

  print(key, end=' ')

  if right != -1:
    inorder(right)
  
def preorder(index):
  # root -> left -> right
  key, left, right = tree[index]
  
  print(key, end=' ')

  if left != -1:
    preorder(left)

  if right != -1:
    preorder(right)

def postorder(index):
  # left -> right -> root
  key, left, right = tree[index]

  if left != -1:
    postorder(left)

  if right != -1:
    postorder(right)
  
  print(key, end=' ')

def main():
  for i in range(n):
    tree.append([int(x) for x in input().split()])

  inorder(0)
  print()
  preorder(0)
  print()
  postorder(0)

n = int(input())
tree = []

threading.Thread(target=main).start()