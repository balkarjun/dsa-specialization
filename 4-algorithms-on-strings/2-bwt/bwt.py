# python3
text = input()

matrix = []
for i in range(len(text)):
  matrix.append(text)
  text = text[-1] + text[:-1]
matrix.sort()

print(''.join([x[-1] for x in matrix]))