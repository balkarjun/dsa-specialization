# python3
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

# both have to be sorted in the same order, and either asc or desc will work
a.sort(reverse=True)
b.sort(reverse=True)

maxValue = 0
for i in range(n):
  maxValue += a[i] * b[i]

print(maxValue)
