# python3

from random import randint

def quicksort(low, high):
  if low > high:
    return
  # array[m1 ... m2] is in its final position
  m1, m2 = partition(low, high)
  quicksort(low, m1 - 1)
  quicksort(m2 + 1, high)

def partition(low, high):
  # pick a pivot at random
  pivotIndex = randint(low, high)
  # swap pivot with first element
  array[low], array[pivotIndex] = array[pivotIndex], array[low]

  pivot = array[low]
  j = low
  k = low
  i = low + 1
  count = 0
  while i <= high:
    if array[i] == pivot:
      j += 1
      array[j], array[i] = array[i], array[j]
      k += 1
      array[j], array[k] = array[k], array[j]
      count += 1
    elif array[i] < pivot:
      j += 1
      array[j], array[i] = array[i], array[j]
    i += 1
  
  while k >= low:
    array[k], array[j] = array[j], array[k]
    k -= 1
    j -= 1
  return [j + 1, j + 1 + count]

n = int(input())
array = [int(x) for x in input().split()]

quicksort(0, len(array) - 1)
print(' '.join([str(x) for x in array]))