# python3
n, m = [int(x) for x in input().split()]

fib = [0, 1]
rem = [0, 1]
flag = False
patternFound = False
pattern = []

for i in range(2, n + 1):
  fib.append(fib[i - 1] + fib[i - 2])
  rem.append(fib[i] % m)

  if rem[i] == 0:
    flag = True
  elif rem[i] == 1 and flag:
    pattern = rem[:-2]
    patternFound = True
    print(pattern)
    break
  else:
    flag = False

if not patternFound:
  print(rem[-1])
else:
  period = len(pattern)
  n = n % period
  print(rem[n])
