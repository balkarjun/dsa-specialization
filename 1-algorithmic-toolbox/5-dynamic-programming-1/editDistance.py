# python3
a = input()
b = input()

n = len(a) + 1
m = len(b) + 1

d = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
  d[i][0] = i

for j in range(m):
  d[0][j] = j  

for i in range(1, n):
  for j in range(1, m):
    if a[i - 1] != b[j - 1]:
      d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + 1)
    else:
      d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1])

print(d[-1][-1])