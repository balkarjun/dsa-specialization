# python3
def nRefills(stops):
  count = 0
  while len(stops) > 1:
    index = 1
    while index < len(stops) and stops[index] - stops[0] <= m:
      index += 1
    # index now points to farthest reachable gas station
    index -= 1
    # cannot move further, so impossible to reach destination
    if index == 0:
      return -1
    count += 1
    stops = stops[index:]
  # decrease count by 1 to exclude 'refill' that took place at destination
  return count - 1

d = int(input()) # total distance to travel
m = int(input()) # distance car can travel on full tank
n = int(input()) # number of gas stations
stops = [int(x) for x in input().split()] # distances at which gas stations are located

# add source and destination as stops, for ease of computation
stops.insert(0, 0)
stops.append(d)

print(nRefills(stops))