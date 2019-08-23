# python3
def compute_prefix_func(text):
  s = [0]
  border = 0
  for i in range(1, len(text)):
    while (border > 0) and (text[i] != text[border]):
      border = s[border - 1]
    if text[i] == text[border]:
      border += 1
    else:
      border = 0
    s.append(border)
  return s

pattern = input()
genome = input()

text = pattern + '$' + genome
prefix = compute_prefix_func(text)

output = []
for i in range(len(pattern) + 1, len(text)):
  if prefix[i] == len(pattern):
    index = i - 2*len(pattern)
    output.append(str(index))

print(' '.join(output))