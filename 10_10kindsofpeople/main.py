# NOTE: This problem is simply a connectivity problem. This solution uses a
#       straightforward implementation of adjacency lists, BFS, and a very
#       simplified version of union-find.

from typing import List
from collections import deque

TAL = List[List[int]]

def create_al(rows: List[str], R: int, C: int):
  al: TAL = [[] for _ in range(R*C)]
  curr_id = 0

  for i in range(R):
    row = rows[i]
    for j in range(C):
      c = row[j]
      if i < R - 1 and rows[i + 1][j] == c: # check south connection
        other_id = curr_id + C
        al[curr_id].append(other_id)
        al[other_id].append(curr_id)
      if j < C - 1 and row[j + 1] == c: # check east connection
        other_id = curr_id + 1
        al[curr_id].append(other_id)
        al[other_id].append(curr_id)
      curr_id += 1
  
  return al

def find_clusters(al: TAL, R: int, C: int):
  curr_cid = 0
  cell_to_cluster = [-1 for _ in range(R*C)]
  
  for i in range(R*C):
    if cell_to_cluster[i] != -1:
      continue
    
    # BFS
    cell_to_cluster[i] = curr_cid
    queue = deque([i])
    while len(queue) > 0:
      curr_cell = queue.popleft()
      for neighbor in al[curr_cell]:
        if cell_to_cluster[neighbor] != -1:
          continue
        cell_to_cluster[neighbor] = curr_cid
        queue.append(neighbor)

    curr_cid += 1
  
  return cell_to_cluster

def rc_to_i(r: int, c: int, C: int):
  return r * C + c

def main():
  R, C = [int(i) for i in input().split()]
  rows = [input() for _ in range(R)]
  al = create_al(rows, R, C)
  cell_to_cluster = find_clusters(al, R, C)

  # answer each query
  n = int(input())
  for _ in range(n):
    r1, c1, r2, c2 = [int(i) - 1 for i in input().split()]
    i1, i2 = rc_to_i(r1, c1, C), rc_to_i(r2, c2, C)
    if cell_to_cluster[i1] != cell_to_cluster[i2]:
      print("neither")
    elif rows[r1][c1] == "1":
      print("decimal")
    else:
      print("binary")

if __name__ == "__main__":
  main()