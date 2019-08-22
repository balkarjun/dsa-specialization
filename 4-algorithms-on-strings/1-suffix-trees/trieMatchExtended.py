# python3
def prefixMatch(start):
  index = start
  node = 0
  while True:
    # if pattern
    if isPattern.get(node, False):
      print(start, end=' ')
      return
    else:
      if index == len(text):
        return
      found = False
      for w in trie[node]:
        if edges[(node, w)] == text[index]:
          found = True
          index += 1
          node = w
          break
      if found == False:
        return

def trieMatch():
  start = 0
  while start < len(text):
    prefixMatch(start)
    start += 1

text = input()
n = int(input())
patterns = [input() for x in range(n)]

# construct trie
isPattern = {}
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
  isPattern[currentNode] = True

trieMatch()