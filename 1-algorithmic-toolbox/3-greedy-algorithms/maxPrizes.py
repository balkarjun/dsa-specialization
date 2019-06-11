# python3
n = int(input())

numbers = []
currentNumber = 1
while n > 0:
  if 2 * currentNumber + 1 > n:
    currentNumber = n
  n -= currentNumber
  numbers.append(currentNumber)
  currentNumber += 1

print(len(numbers))
print(' '.join([str(x) for x in numbers]))