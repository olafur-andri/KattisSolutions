from typing import List, Tuple
from heapq import heappush, heappop

TPQ = List[Tuple[float, int]]
TAL = List[List[Tuple[int, float]]]

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

    for neighbor, dist in al[curr_vertex]:
      if visited[neighbor]:
        continue
      old_cost = D[neighbor]
      new_cost = D[curr_vertex] + dist
      if new_cost < old_cost:
        heappush(pq, (new_cost, neighbor))
        D[neighbor] = new_cost
        parent[neighbor] = curr_vertex
  
  return D, parent
