from collections import deque
from typing import Deque, Dict, List, Tuple


TAL = Dict[str, List[str]]

def bfs(al: TAL, start_node: str):
  visited: Dict[str, bool] = { key: False for key in al }
  parent: Dict[str, str] = {}
  queue: Deque[str] = deque()
  visited[start_node] = True
  found_cycle = False
  queue.append(start_node)

  while queue:
    v = queue.popleft()
    for neighbor in al[v]:
      if neighbor == start_node:
        found_cycle = True
        parent[neighbor] = v
        break
      if visited[neighbor]:
        continue
      visited[neighbor] = True
      queue.append(neighbor)
      parent[neighbor] = v
  
  return found_cycle, parent

def find_cycle(vertex: str, al: TAL):
  found, parent = bfs(al, vertex)
  if found:
    curr_vertex = vertex
    path: List[str] = [curr_vertex]
    while parent[curr_vertex] != vertex:
      curr_vertex = parent[curr_vertex]
      path.append(curr_vertex)
    return list(reversed(path))
  else:
    return []

def main():
  N = int(input())
  names = input().split()
  al: TAL = { name: [] for name in names }

  # create the graph
  for _ in range(N):
    current_vertex, k = input().split()
    k = int(k)
    for _ in range(k):
      line = input()[7::]
      neighbors = line.split(", ")
      al[current_vertex].extend(neighbors)
  
  # run BFS from each vertex to find a shortest cycle
  # TODO: optimize by discarding paths that are already longer than the shortest recorded cycle
  shortest_cycle_length = float("inf")
  shortest_cycle: List[str] = []
  for vertex in al:
    cycle = find_cycle(vertex, al)
    if len(cycle) > 0 and len(cycle) < shortest_cycle_length:
      shortest_cycle_length = len(cycle)
      shortest_cycle = cycle
  
  if shortest_cycle_length == float("inf"):
    print("SHIP IT")
  else:
    print(" ".join(shortest_cycle))

if __name__ == "__main__":
  main()