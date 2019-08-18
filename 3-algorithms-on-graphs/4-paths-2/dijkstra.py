# python3
import heapq

def solve():
  # create adjacency list
  for i in range(m):
    u, v, w = [int(x) for x in input().split()]
    graph[u].append(v)
    weights[(u, v)] = w
  
  u, v = [int(x) for x in input().split()]

  dist = dijkstra(u)[v]
  if dist == INF:
    return -1
  return dist

def dijkstra(s):
  dist = [INF for x in range(n + 1)]
  dist[s] = 0

  heap = [[dist[node], node] for node in range(n + 1)]
  heapq.heapify(heap)

  while len(heap) > 1:
    d, node = heapq.heappop(heap)
    # for each neighbour
    for w in graph[node]:
      if dist[w] > dist[node] + weights[(node, w)]:
        dist[w] = dist[node] + weights[(node, w)]
        heapq.heappush(heap, [dist[w], w])
  return dist

INF = 10**9
n, m = [int(x) for x in input().split()]
graph = [[] for x in range(n + 1)]
weights = {}

print(solve())