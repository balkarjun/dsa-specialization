# python3
def diff(array):
  return array[0] - array[1]

def prod(array):
  return array[0] * array[1]

# compute min and max values of subexpression i->j : di opi ... opj-1 dj
def optimalValues(i, j):
  minValue = 10**8
  maxValue = -10**8

  for k in range(i, j):
    maxLeft = M[i][k]
    minLeft = m[i][k]
    maxRight = M[k + 1][j]
    minRight = m[k + 1][j]

    array = [[maxLeft, maxRight], [maxLeft, minRight], [minLeft, maxRight], [minLeft, minRight]]

    if operations[k] == '+':
      a, b, c, d = [sum(x) for x in array]
    elif operations[k] == '-':
      a, b, c, d = [diff(x) for x in array]
    else:
      a, b, c, d = [prod(x) for x in array]
    
    minValue = min(minValue, a, b, c, d)
    maxValue = max(maxValue, a, b, c, d)
  return [minValue, maxValue]

def solve():
  # max and min value of a single digit is the digit itself
  for i in range(length):
    m[i][i] = digits[i]
    M[i][i] = digits[i]
  
  # move diagonally
  for j in range(1, length):
    for i in range(length - j):
      m[i][i + j], M[i][i + j] = optimalValues(i, i + j)

  return M[0][-1]


rawInput = input()

digits = []
operations = []
for i in range(len(rawInput)):
  # digits are at even positions
  if i % 2 == 0:
    digits.append(int(rawInput[i]))
  else:
    operations.append(rawInput[i])

# matrix of size n*n
length = len(digits)
M = [[0 for x in range(length)] for x in range(length)]
m = [[0 for x in range(length)] for x in range(length)]

print(solve())