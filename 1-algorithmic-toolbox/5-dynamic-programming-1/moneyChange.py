# python3
money = int(input())

minCoins = [0]
for m in range(1, money + 1):
  currentMin = min([minCoins[m - d] + 1 for d in [1, 3, 4] if m >= d])
  minCoins.append(currentMin)

print(minCoins[-1])
