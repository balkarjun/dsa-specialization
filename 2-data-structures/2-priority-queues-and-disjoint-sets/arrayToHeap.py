# python3

def left(i):
  return 2*i + 1

def right(i):
  return 2*i + 2

def parent(i):
  return (i - 1)//2

def hasLeftChild(i):
  return left(i) < size

def hasRightChild(i):
  return right(i) < size

def isInvalid(i):
  return (hasLeftChild(i) and nodes[i] > nodes[left(i)]) or (hasRightChild(i) and nodes[i] > nodes[right(i)])

def siftDown(parent):
  # check if heap property is violated
  if not isInvalid(parent):
    return
  
  minChildIndex = 0
  # find index of smaller child
  if hasLeftChild(parent):
    minChildIndex = left(parent)
  if hasRightChild(parent) and nodes[right(parent)] < nodes[left(parent)]:
    minChildIndex = right(parent)
  
  # swap parent with smaller child
  nodes[parent], nodes[minChildIndex] = nodes[minChildIndex], nodes[parent]
  swaps.append([parent, minChildIndex])
  
  # sift on smaller child
  siftDown(minChildIndex)

def main():
  for i in range(size - 1, -1, -1):
    if hasLeftChild(i) or hasRightChild(i):
      siftDown(i)
  
  print(len(swaps))
  for swap in swaps:
    print(swap[0], swap[1])

size = int(input())
nodes = [int(x) for x in input().split()]
swaps = []
main()