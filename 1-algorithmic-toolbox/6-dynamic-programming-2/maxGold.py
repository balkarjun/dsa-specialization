# python3

# knapsack capacity, number of gold bars
capacity, nBars = [int(x) for x in input().split()]
# weights of gold bars
weights = [int(x) for x in input().split()]

# initialize (capacity + 1) x (nBars + 1) matrix
matrix = [[0 for i in range(nBars + 1)] for j in range(capacity + 1)]

for w in range(1, capacity + 1):
  for v in range(1, nBars + 1):
    # value (weight) of vth bar
    value = weights[v - 1]
    # optimal value if vth bar is present in solution
    a = -1
    if w >= value:
      a = matrix[w - value][v - 1] + value
    # optimal value if vth bar not present in solution
    b = matrix[w][v - 1]

    matrix[w][v] = max(a, b)

print(matrix[-1][-1])
