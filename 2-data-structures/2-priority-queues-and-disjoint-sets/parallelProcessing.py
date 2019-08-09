# python3
import heapq

threads, jobs = [int(x) for x in input().split()]
# time to process ith job
times = [int(x) for x in input().split()]

# create heap containing [next_free_time, thread_index]
heap = [[0, i] for i in range(threads)]
heapq.heapify(heap)

for job_time in times:
  # get next free thread
  thread = heapq.heappop(heap)
  print(thread[1], thread[0])
  # assign job and store next free time
  thread[0] += job_time
  # add it back to heap
  heapq.heappush(heap, thread)