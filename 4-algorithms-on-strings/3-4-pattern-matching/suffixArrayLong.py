# python3

# Sort cyclic shifts of size 1
def sort_char(s):
  order = [0 for x in range(len(s))]
  count = [0 for x in range(ALPHA_SIZE)]

  for char in s:
    code = ord(char) - OFFSET
    count[code] += 1
  for i in range(1, ALPHA_SIZE):
    count[i] += count[i - 1]

  for i in range(len(s) - 1, -1, -1):
    code = ord(s[i]) - OFFSET
    count[code] -= 1
    order[count[code]] = i
  
  return order

def compute_char_class(s, order):
  c = [0 for x in range(len(s))]

  for i in range(1, len(s)):
    cur, prev = order[i], order[i - 1]
    
    if s[cur] != s[prev]:
      c[cur] = c[prev] + 1
    else:
      c[cur] = c[prev]
  
  return c

# Sort cyclic shifts of size 2*L
def sort_doubled(s, l, order, c):
  count = [0 for x in range(len(s))]
  new_order = [0 for x in range(len(s))]

  for i in range(len(s)):
    count[c[i]] += 1
  for i in range(1, len(s)):
    count[i] += count[i - 1]
  
  for i in range(len(s) - 1, -1, -1):
    start = (order[i] - l + len(s)) % (len(s))
    cl = c[start]
    count[cl] -= 1
    new_order[count[cl]] = start
  return new_order

def update_classes(new_order, c, l):
  n = len(new_order)
  new_c = [0 for x in range(n)]
  
  for i in range(1, n):
    cur, prev = new_order[i], new_order[i - 1]
    mid, mid_prev = (cur + l) % n, (prev + l) % n

    if c[cur] != c[prev] or c[mid] != c[mid_prev]:
      new_c[cur] = new_c[prev] + 1
    else:
      new_c[cur] = new_c[prev]
  return new_c

def build_suffix_array(s):
  order = sort_char(s)
  c = compute_char_class(s, order)
  l = 1

  while l < len(s):
    order = sort_doubled(s, l, order, c)
    c = update_classes(order, c, l)
    l *= 2
  
  return order

# A-Z, @
ALPHA_SIZE = 27
# ord('@') = 64
OFFSET = 64

text = input()
# replace $ with @
text = text[:-1] + '@'

suffix_array = build_suffix_array(text)
print(' '.join([str(x) for x in suffix_array]))