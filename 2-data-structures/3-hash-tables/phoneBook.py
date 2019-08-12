# python3

n = int(input())
phone_book = {}

for i in range(n):
  query = [x for x in input().split()]

  if query[0] == 'add':
    phone_book[query[1]] = query[2]
  elif query[0] == 'del':
    if phone_book.get(query[1]):
      del phone_book[query[1]]
  else:
    print(phone_book.get(query[1], 'not found'))
