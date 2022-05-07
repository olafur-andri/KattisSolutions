from typing import Deque, List
from collections import deque


TAL = List[List[int]]

def bfs(al: TAL, start_node: int):
  visited: List[bool] = [False] * len(al)
  queue: Deque[int] = deque()
  visited[start_node] = True
  queue.append(start_node)

  while queue:
    s = queue.popleft()
    for neighbor in al[s]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append(neighbor)