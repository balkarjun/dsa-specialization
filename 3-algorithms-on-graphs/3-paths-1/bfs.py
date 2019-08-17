# python3
import queue

def solve():
  # create adjacency list
  for i in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

  u, v = [int(x) for x in input().split()]

  dist = bfs(u)
  return dist[v]

def bfs(s):
  dist = [-1 for x in range(n + 1)]

  dist[s] = 0
  q = queue.Queue(maxsize=n)
  q.put(s)

  while not q.empty():
    u = q.get()
    # for all neighbours of u
    for w in graph[u]:
      # if undiscovered
      if dist[w] == -1:
        q.put(w)
        dist[w] = dist[u] + 1
  return dist

n, m = [int(x) for x in input().split()]
graph = [[] for x in range(n + 1)]
visited = [False for x in range(n + 1)]

print(solve())
