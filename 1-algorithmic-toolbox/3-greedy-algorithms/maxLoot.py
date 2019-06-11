# python3
n, W = [int(x) for x in input().split()]

items = []
for i in range(n):
  value, weight = [int(x) for x in input().split()]
  items.append([value, weight, value/weight])

# sort by decreasing unit value
items.sort(key = lambda x : x[2], reverse=True)

totalValue = 0
maxValueIndex = 0
while maxValueIndex < len(items) and W > 0:
  # fill knapsack with 1 unit of max value item
  W -= 1
  items[maxValueIndex][1] -= 1
  totalValue += items[maxValueIndex][2]
  # if max unit value item is depleted, move to next one
  if items[maxValueIndex][1] == 0:
    maxValueIndex += 1

print(totalValue)