# python3
m = int(input())

count = 0
while m >= 1:
  d = 1
  if m >= 10:
    d = 10
  elif m >= 5:
    d = 5
  m -= d
  count += 1

print(count)
