from typing import Deque, List, Tuple
from operator import itemgetter
from collections import deque

THeights = List[Tuple[int, int]]

def get_neighbors(heights: THeights, w: int, i: int):
  neighbors: THeights = []
  if i - w >= 0:
    neighbors.append(heights[i - w])
  if i + w < len(heights):
    neighbors.append(heights[i + w])
  if (i+1) % w != 0:
    neighbors.append(heights[i + 1])
  if i % w != 0:
    neighbors.append(heights[i - 1])
  return neighbors

def flood_fill(heights: THeights, reached: List[bool], w: int, i: int):
  q: Deque[int] = deque([i])
  reached[i] = True
  while len(q) > 0:
    c_index = q.popleft()
    c_height = heights[c_index][1]
    neighbors = get_neighbors(heights, w, c_index)
    for n_index, n_height in neighbors:
      if reached[n_index]:
        continue
      if n_height > c_height:
        continue
      reached[n_index] = True
      q.append(n_index)

def main():
  # read in grid dimensions
  h, w = map(int, input().split())

  # read in heights with reference to their original index
  heights: THeights = [None] * (h*w) # index, height
  j = 0
  for _ in range(h):
    row = map(int, input().split())
    for height in row:
      heights[j] = (j, height)
      j += 1
  
  # sort the heights in descending order
  desc_heights = sorted(heights, key=itemgetter(1), reverse=True)

  # set all tiles with heights 0 or 1 as reached
  reached = [False] * (h*w)
  for index, height in heights:
    reached[index] = height < 2

  # loop through heights in descending order, once we find an unreached height,
  # then place an elevator there
  nr_elevators = 0
  for index, height in desc_heights:
    if reached[index]:
      continue
    flood_fill(heights, reached, w, index)
    nr_elevators += 1

  print(nr_elevators)
  

if __name__ == "__main__":
  main()