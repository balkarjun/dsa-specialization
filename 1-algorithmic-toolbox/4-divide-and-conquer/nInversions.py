# python3

def mergeSort(array):
  if len(array) == 1:
    return [array, 0]

  mid = len(array) // 2
  left, lInversions = mergeSort(array[:mid])
  right, rInversions = mergeSort(array[mid:])
  merged, swapInversions =  merge(left, right)

  return [merged, lInversions + rInversions + swapInversions]

def merge(left, right):
  l, r = 0, 0
  result = []
  inversions = 0

  while l < len(left) and r < len(right):
    if left[l] > right[r]:
      inversions += len(left) - l
      result.append(right[r])
      r += 1
    else:
      result.append(left[l])
      l += 1

  while l < len(left):
    result.append(left[l])
    l += 1

  while r < len(right):
    result.append(right[r])
    r += 1

  return [result, inversions]

n = int(input())
array = [int(x) for x in input().split()]

print(mergeSort(array)[1])
