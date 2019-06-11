# python3

def binarySearch(array, key):
  low = 0
  high = len(array) - 1

  while low <= high:
    midIndex = (low + high)//2

    if key == array[midIndex]:
      return midIndex
    elif key > array[midIndex]:
      low = midIndex + 1
    else:
      high = midIndex - 1
  return -1

n = [int(x) for x in input().split()][1:]
k = [int(x) for x in input().split()][1:]

for i in k:
  print(binarySearch(n, i), end=' ')