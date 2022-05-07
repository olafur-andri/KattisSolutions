from typing import List

def binary_search(array, x):
  # Repeat until the pointers low and high meet each other
  low = 0
  high = len(array) - 1
  while low <= high:
    mid = low + (high - low)//2
    if array[mid] == x:
      return mid
    elif array[mid] < x:
      low = mid + 1
    else:
      high = mid - 1
  return low

def main():
  n, m = [int(i) for i in input().split()]

  # collect bucket sizes
  buckets: List[int] = [-1] * n
  for i in range(n):
    buckets[i] = int(input())
  
  # collect microliters for each color
  colors: List[int] = [-1] * m
  for i in range(m):
    colors[i] = int(input())
  
  # sort the buckets
  buckets.sort()

  # calculate minimum waste
  waste = 0
  for color in colors:
    min_index = binary_search(buckets, color)
    min_bucket = buckets[min_index]
    min_waste = min_bucket - color
    waste += min_waste
  
  print(waste)

if __name__ == "__main__":
  main()