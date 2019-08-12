# python3

def h(s):
  p = 1000000007
  x = 263

  res = 0
  for i in range(len(s)):
    # ascii value of s[i]
    value = ord(s[i])
    res += value * (x**i)
  return (res%p)%m

def find(string):
  key = h(string)
  for value in table[key]:
    if value == string:
      return 'yes'
  return 'no'

def add(string):
  if find(string) == 'yes':
    return
  key = h(string)
  table[key].insert(0, string)

def delete(string):
  key = h(string)
  for i in range(len(table[key])):
    value = table[key][i]
    if value == string:
      del table[key][i]
      return

def check(index):
  return ' '.join(table[index])

def main():
  for i in range(n):
    first, second = [x for x in input().split()]

    if first == 'add':
      add(second)
    elif first == 'del':
      delete(second)
    elif first == 'find':
      print(find(second))
    else:
      print(check(int(second)))

m = int(input())
n = int(input())

table = [[] for x in range(m)]

main()