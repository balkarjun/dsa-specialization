# python3
n = int(input())

steps = [[], [1]]
for k in range(2, n + 1):
  a, b = 10**8, 10**8
  if k >= 2 and k % 2 == 0:
    a = len(steps[k//2]) + 1
  if k >= 3 and k % 3 == 0:
    b = len(steps[k//3]) + 1
  c = len(steps[k - 1]) + 1

  if a <= b and a <= c:
    steps.append(steps[k//2] + [k])
  elif b < a and b < c:
    steps.append(steps[k//3] + [k])
  else:
    steps.append(steps[k - 1] + [k])

print(len(steps[-1]) - 1)
print(' '.join([str(x) for x in steps[-1]]))