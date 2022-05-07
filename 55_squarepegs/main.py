import math
from typing import Set

def find_min_radius(L):
  l = L / 2
  return math.sqrt((l**2) + (l**2))

def main():
  N, M, K = [int(i) for i in input().split()]
  plot_radii = list(map(int, input().split()))
  house_radii = list(map(int, input().split()))
  square_lengths = list(map(int, input().split()))

  # translate all square lengths over to house_radii
  for L in square_lengths:
    house_radii.append(find_min_radius(L))
  
  # sort both the house and plot radii
  house_radii.sort()
  plot_radii.sort()

  # fit the smallest houses to each plot
  filled_houses: Set[int] = set()
  for plot_radius in plot_radii:
    for i, house_radius in enumerate(house_radii):
      if house_radius >= plot_radius:
        break
      if i in filled_houses:
        continue
      filled_houses.add(i)
      break
  
  print(len(filled_houses))
  

if __name__ == "__main__":
  main()