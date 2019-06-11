# python3

# Pisano pattern an period for mod 10
pattern = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
period = len(pattern)

n = int(input())

# fib(0) + ... + fib(n) = fib(n + 2) - 1
target = (n + 2) % period

# (a - 1) % 10 = (a % 10 - 1) % 10
result = (pattern[target] - 1) % 10
print(result)