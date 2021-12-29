import sys
from typing import Dict, Tuple

# `m` is # printers and `d` is # days
def simulate(n: int, m: int, d: int):
  if n <= 0:
    return d
  
  # try not printing a new printer
  no_new_printer = simulate(n - m, m, d + 1)

  # try printing a new printer (as long as it's sensible)
  add_new_printer = float("inf")
  if m < n:
    add_new_printer = simulate(n, m + 1, d + 1)

  # return the better solution
  solution = min(no_new_printer, add_new_printer)
  return solution

def solve_brute(n: int):
  return simulate(n, m=1, d=0)

def main():
  n = int(input())
  print(solve_brute(n))

if __name__ == "__main__":
  sys.setrecursionlimit(1_000_000)
  main()