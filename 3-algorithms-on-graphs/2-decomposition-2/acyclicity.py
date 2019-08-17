# python3

'''
If G is a DAG with edge u to v, post(u) > post(v)
statement p => q : DAG => post(u) > post(v) for u, v in G
contrapositive ~q => ~p : post(u) <= post(v) => ~DAG for u, v in G
'''

def solve():
  edge_list = []
  # create adjacency and edge lists
  for i in range(m):
    u, v = [int(x) for x in input().split()]
    edge_list.append([u, v])
    graph[u].append(v)
  
  # find post values
  for vertex in range(1, n + 1):
    if visited[vertex] == False:
      explore(vertex)
  
  # check if DAG
  for u, v in edge_list:
    if post[u] <= post[v]:
      return 1
  return 0

def explore(vertex):
  global clock
  visited[vertex] = True
  clock += 1
  # for each neighbour of vertex
  for w in graph[vertex]:
    if visited[w] == False:
      explore(w)
  post[vertex] = clock
  clock += 1

n, m = [int(x) for x in input().split()]
graph = [[] for x in range(n + 1)]
visited = [False for x in range(n + 1)]
clock = 1
post = [0 for x in range(n + 1)]

print(solve())
