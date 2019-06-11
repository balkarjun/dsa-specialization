# python3
if __name__ == '__main__':
  n = input()
  numbers = sorted([int(x) for x in input().split()], reverse=True)
  print(numbers[0]*numbers[1])
