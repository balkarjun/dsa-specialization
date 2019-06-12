# python3

def hasMajority(array, n):
  prevNum = -1
  count = 1
  for currNum in array:
    if currNum != prevNum:
      count = 1
      prevNum = currNum
    else:
      count += 1
    if count > n//2:
      return 1
  return 0  

n = int(input())
a = [int(x) for x in input().split()]
a.sort()

print(hasMajority(a, n))