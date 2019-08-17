# python3

def solve():
  # create adjacency list
  for i in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
  
  for vertex in range(1, n + 1):
    if visited[vertex] == False:
      explore(vertex)

def explore(vertex):
  visited[vertex] = True

  for w in graph[vertex]:
    if visited[w] == False:
      explore(w)
  result.append(vertex)

n, m = [int(x) for x in input().split()]
graph = [[] for x in range(n + 1)]
visited = [False for x in range(n + 1)]
result = []

solve()
print(' '.join(str(x) for x in result[::-1]))