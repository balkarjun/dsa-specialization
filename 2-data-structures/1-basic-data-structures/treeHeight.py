# python3

n = int(input())
nodes = [[int(x), 0] for x in input().split()]

maxHeight = -1
for index in range(n):
  path = [index]
  parent = nodes[index][0]
  height = 1

  while parent != -1:
    if nodes[parent][1] != 0:
      height += nodes[parent][1]
      break
    path.append(parent)
    parent = nodes[parent][0]
    height += 1
  
  maxHeight = max(maxHeight, height)
  for k in path:
    nodes[k][1] = height
    height -= 1

print(maxHeight)
