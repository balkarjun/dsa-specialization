# python3
n = int(input())
patterns = [input() for x in range(n)]

trie = {0: []}
edges = {}
for pattern in patterns:
  currentNode = 0
  for char in pattern:
    found = False
    for w in trie[currentNode]:
      if edges[(currentNode, w)] == char:
        currentNode = w
        found = True
        break
    if found == False:
      newNode = len(trie)
      trie[currentNode].append(newNode)
      trie[newNode] = []
      edges[(currentNode, newNode)] = char
      currentNode = newNode

for key in edges:
  print('{}->{}:{}'.format(key[0], key[1], edges[key]))
