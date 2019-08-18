# python3

def solve():
  INF = 10**9

  n, m = [int(x) for x in input().split()]
  edge_list = []
  for i in range(m):
    edge_list.append([int(x) for x in input().split()])

  dist = [INF for x in range(n + 1)]
  dist[1] = 0

  for i in range(n):
    for u, v, w in edge_list:
      if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        # If relaxed at nth iteration
        if i == n - 1:
          return 1
  return 0

print(solve())