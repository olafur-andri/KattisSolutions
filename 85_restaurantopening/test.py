import math
from typing import List, Union
from pprint import pprint
from main import get_total_distance, get_grid_dimensions, read_in_grid, gradient_descent
from random import randrange

def get_random_grid(n: int, m: int):
  grid: List[List[int]] = []
  for _ in range(n):
    row: List[int] = []
    for _ in range(m):
      row.append(randrange(0, 51))
    grid.append(row)
  return grid

def get_centroid(grid: List[List[int]]):
  n, m = get_grid_dimensions(grid)
  total_population = sum( [sum(row) for row in grid] )
  fractions = [[p / total_population for p in row] for row in grid]

  # get a weighted row and column index
  wr, wc = 0, 0
  for r in range(n):
    for c in range(m):
      wr += r * fractions[r][c]
      wc += c * fractions[r][c]
  
  # get centroid row and column by flooring both weighted values
  return round(wr), round(wc)

def brute():
  min_dist = 0
  centroid_dist = 0
  grad_dist = 0

  n, m = map(int, input().split())

  while grad_dist == min_dist:
    grid = get_random_grid(n, m)
    # grid = read_in_grid()
    print("============")
    print("=== GRID ===")
    print("============")
    pprint(grid)

    # create a container for the calculated total distances
    n, m = get_grid_dimensions(grid)
    total_distances: List[List[Union[int, float]]] = [ [0] * m for _ in range(n) ]

    # calculate total distances for each cell
    for r in range(n):
      for c in range(m):
        total_distances[r][c] = get_total_distance(grid, r, c)
    
    # print out total distances
    print()
    print("=======================")
    print("=== TOTAL DISTANCES ===")
    print("=======================")
    pprint(total_distances)

    min_dist = min( [min(row) for row in total_distances] )
    print(f"min dist: {min_dist}")

    centroid_r, centroid_c = get_centroid(grid)
    centroid_dist = total_distances[centroid_r][centroid_c]
    print(f"centroid: {centroid_dist}")

    grad_dist = gradient_descent(grid)
    print(f"gradient dist: {grad_dist}")


if __name__ == "__main__":
  brute()
