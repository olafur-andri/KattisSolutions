import math
from typing import List

def find_lowest_divisor(n: int):
  threshold = math.floor(math.sqrt(n))
  for i in range(2, threshold + 1):
    if n % i == 0:
      return i
  return -1

def find_factors(X: int):
  factors: List[int] = []
  curr = X
  while True:
    lowest_divisor = find_lowest_divisor(curr)
    if lowest_divisor == -1: # `curr` is prime
      factors.append(curr)
      break
    factors.append(lowest_divisor)
    curr = curr // lowest_divisor
  return factors

def main():
  X = int(input())
  factors = find_factors(X)
  print(len(factors))

if __name__ == "__main__":
  main()