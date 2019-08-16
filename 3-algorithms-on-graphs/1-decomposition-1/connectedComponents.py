# python3

def solve():
  # create adjacency list
  for i in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

  count = 0
  for vertex in range(1, n + 1):
    if visited[vertex] == False:
      explore(vertex)
      count += 1
  
  return count

def explore(vertex):
  visited[vertex] = True
  # for each neighbour of vertex
  for w in graph[vertex]:
    if visited[w] == False:
      explore(w)

n, m = [int(x) for x in input().split()]
graph = [[] for x in range(n + 1)]
visited = [False for x in range(n + 1)]

print(solve())
