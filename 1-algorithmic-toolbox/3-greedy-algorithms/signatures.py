# python3
n = int(input())
segments = []
for i in range(n):
  segments.append([int(x) for x in input().split()])

# sort pairs (a, b) in ascending order of b
segments.sort(key = lambda x : x[1])

currentIndex = 0
coordinates = []
while currentIndex < len(segments):
  coordinate = segments[currentIndex][1]
  newIndex = currentIndex + 1
  coordinates.append(coordinate)
  while newIndex < len(segments) and segments[newIndex][0] <= coordinate <= segments[newIndex][1]:
    newIndex += 1
  currentIndex = newIndex

print(len(coordinates))
print(' '.join([str(x) for x in coordinates]))