from typing import List, Tuple

# GLOBAL VARIABLES
total_distances: List[List[int]] = [] # cache total_distance calculations

def get_grid_dimensions(grid: List[List[int]]):
  return len(grid), len(grid[0])

def read_in_grid():
  n, _ = map(int, input().split())
  grid: List[List[int]] = []
  for i in range(n):
    grid.append(list(map(int, input().split())))
  return grid

def manhattan(r1: int, c1: int, r2: int, c2: int):
  return abs(r2 - r1) + abs(c2 - c1)

def get_total_distance(grid: List[List[int]], r1: int, c1: int):
  global total_distances
  should_cache = len(total_distances) > 0

  # return infinity if the index is invalid
  n, m = get_grid_dimensions(grid)
  r1_invalid = r1 < 0 or r1 >= n
  c1_invalid = c1 < 0 or c1 >= m
  if r1_invalid or c1_invalid:
    return float("inf")

  # return cached result if it exists
  if should_cache and total_distances[r1][c1] != -1:
    return total_distances[r1][c1]

  # calculate total manhattan distance from every cell to this one
  total_distance = 0
  n, m = get_grid_dimensions(grid)
  for r2 in range(n):
    for c2 in range(m):
      population = grid[r2][c2]
      total_distance += population * manhattan(r1, c1, r2, c2)
  
  if should_cache:
    total_distances[r1][c1] = total_distance
  return total_distance

def gradient_descent(grid: List[List[int]]):
  global total_distances

  # initialize cache
  n, m = get_grid_dimensions(grid)
  total_distances = [([-1] * m) for _ in range(n)]

  # start in the top-left corner
  r, c = 0, 0 # row-column cursor

  # run as long as we haven't found a minima
  is_minima = False
  opt_total_dist = float("inf")
  while not is_minima:
    curr_total_dist = get_total_distance(grid, r, c)
    neighbor_coords: List[Tuple[int, int]] = [
      (r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1),
    ]

    # find an optimal orthogonal neighbor that is more optimal than me
    opt_total_dist = curr_total_dist
    opt_coords = (r, c)
    for neighbor_r, neighbor_c in neighbor_coords:
      neighbor_total_dist = get_total_distance(grid, neighbor_r, neighbor_c)
      if neighbor_total_dist < opt_total_dist:
        opt_total_dist = neighbor_total_dist
        opt_coords = (neighbor_r, neighbor_c)

    # check whether I am a minima
    is_minima = opt_total_dist >= curr_total_dist

    # update cursor
    r, c = opt_coords

  return opt_total_dist

def main():
  grid = read_in_grid()
  print(gradient_descent(grid))
  

if __name__ == "__main__":
  main()