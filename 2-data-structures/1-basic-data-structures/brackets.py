# python3

def solve():
  for index in range(len(string)):
    char = string[index]

    # push opening brackets to stack
    if char in pair.keys():
      stack.append([char, index])
    elif char in pair.values():
      # if closing bracket matches with element at top of stack, pair exists
      if len(stack) > 0 and pair[stack[-1][0]] == char:
        stack.pop()
      # otherwise, unmatched closing bracket exists
      else:
        return index + 1

  # If stack is not empty, unmatched opening bracket exists
  if len(stack) != 0:
    return stack[0][1] + 1
  else:
    return 'Success'

string = input()
stack = []
pair = {'[':']', '{':'}', '(':')'}

print(solve())