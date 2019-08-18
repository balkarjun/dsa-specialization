# python3
import heapq

def create_graph():
  points = [None]
  for i in range(n):
    x, y = [int(x) for x in input().split()]
    points.append([x, y])

  for u in range(1, n + 1):
    for v in range(1, n + 1):
      if u != v:
        graph[u].append(v)
        x1, y1 = points[u]
        x2, y2 = points[v]
        weights[(u, v)] = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def dijkstra():
  cost = [INF for x in range(n + 1)]
  cost[1] = 0

  heap = [[cost[node], node] for node in range(n + 1)]
  heapq.heapify(heap)

  cleared = {}
  while len(heap) > 1:
    c, node = heapq.heappop(heap)
    cleared[node] = True

    # for each neighbour
    for w in graph[node]:
      if cleared.get(w, False) == False and cost[w] > weights[(node, w)]:
        cost[w] = weights[(node, w)]
        heapq.heappush(heap, [cost[w], w])
  return cost

INF = 10**9
n = int(input())
graph = [[] for x in range(n + 1)]
weights = {}

create_graph()
print(sum(dijkstra()[1:]))
