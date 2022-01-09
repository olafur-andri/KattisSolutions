from typing import Dict, List, Tuple
from heapq import heappush, heappop

TPQ = List[Tuple[float, int]]
TDayPQ = List[Tuple[float, int, int]]
TAL = Dict[int, Dict[int, float]]

def dijkstra(al: TAL, start: int):
  n = len(al)
  D = [float("inf")] * n
  parent = [-1] * n
  visited = [False] * n
  pq: TPQ = []

  D[start] = 0
  heappush(pq, (0, start))

  while pq:
    _, curr_vertex = heappop(pq)
    visited[curr_vertex] = True

    for neighbor, dist in al[curr_vertex].items():
      if visited[neighbor]:
        continue
      old_cost = D[neighbor]
      new_cost = D[curr_vertex] + dist
      if new_cost < old_cost:
        heappush(pq, (new_cost, neighbor))
        D[neighbor] = new_cost
        parent[neighbor] = curr_vertex
  
  return D, parent

def knightstra(al: TAL, start: int):
  n = len(al)
  D = [float("inf")] * n
  visited = [False] * n
  pq: TPQ = []

  D[start] = 0
  heappush(pq, (0, start, 12))

  while pq:
    _, curr_vertex, ttw = heappop(pq) # ttw: time left to walk
    visited[curr_vertex] = True

    for neighbor, dist in al[curr_vertex].items():
      if visited[neighbor]:
        continue
      old_cost = D[neighbor]
      new_cost = D[curr_vertex] + dist
      new_ttw = ttw - dist
      if dist > ttw: # need to sleep
        new_cost += 12
        new_ttw += 12
      if new_cost < old_cost:
        heappush(pq, (new_cost, neighbor, new_ttw))
        D[neighbor] = new_cost
  
  return D

def time_til_0800(t: int):
  if t <= 8: return 8 - t
  else:      return 8 - t + 24

def daykstra(al: TAL, start: int):
  n = len(al)
  D = [float("inf")] * n
  visited = [False] * n
  pq: TDayPQ = []

  D[start] = 0
  heappush(pq, (0, start, 8))

  while pq:
    _, curr_vertex, time = heappop(pq)
    ttw = 20 - time
    visited[curr_vertex] = True

    for neighbor, dist in al[curr_vertex].items():
      if visited[neighbor]:
        continue
      old_cost = D[neighbor]
      new_cost = D[curr_vertex] + dist
      new_time = time + dist
      if dist > ttw: # need to sleep
        tt8 = time_til_0800(time)
        new_cost += tt8
        new_time = 8 + dist
      if new_cost < old_cost:
        heappush(pq, (new_cost, neighbor, new_time))
        D[neighbor] = new_cost
  
  return D

def main():
  n, m = list(map(int, input().split()))
  al: TAL = {i: {} for i in range(n)}

  # read in the edges
  for _ in range(m):
    u, v, d = list(map(int, input().split()))
    al[u][v] = d
    al[v][u] = d

  # Dr. Knight is simple to follow. A clean call to Dijkstra's algorithm will
  # give us the path she'll walk. She walks as much as she can, until 12 hours
  # have passed. Then she sleeps for 12 hours. D[n-1] // 12 tells us how often
  # she had to sleep during her trip.
  D_knight = knightstra(al, 0)
  dr_knight = D_knight[n-1] # + ( (D[n-1] - 1 // 12) * 12 )

  # Mr. Day is a bit more complicated. He stops his walking once he realizes he
  # won't be able to make it to the next cabin. This means that if the technical
  # shortest path has a lot of cabins, taking a different path might actually
  # result in a shorter path. Need a modified Dijkstra algorithm to reflect
  # Mr. Day's movements.
  D_day = daykstra(al, 0)
  mr_day = D_day[n-1]

  # print(f"Dr. Knight: {dr_knight} hours")
  # print(f"Mr. Day:    {mr_day} hours")

  print(mr_day - dr_knight)

if __name__ == "__main__":
  main()