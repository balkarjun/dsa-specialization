# python3
from functools import cmp_to_key

def compare(a, b):
  aFirst = int(str(a) + str(b))
  bFirst = int(str(b) + str(a))
  return bFirst - aFirst

n = int(input())
a = [int(x) for x in input().split()]

result = [str(x) for x in sorted(a, key=cmp_to_key(compare))]
print(''.join(result))
