from math import ceil, floor
from typing import Deque, List, Tuple, Union
from collections import deque

TOps = Tuple[str, str, str]

OPS = ("+", "-", "*", "/")

def evaluate(o1: str, o2: str, o3: str) -> int:
  s = stringify(o1, o2, o3)
  res = round(eval(s))
  return res

def stringify(o1: str, o2: str, o3: str):
  return f"4 {o1} 4 {o2} 4 {o3} 4"

def main():
  # build cache of all possible assignments of operations
  M: List[Union[TOps, None]] = [None] * 1_000
  for o1 in OPS:
    for o2 in OPS:
      for o3 in OPS:
        M[evaluate(o1, o2, o3)] = (o1, o2, o3)
  
  for i in range(-60, 257):
    print(str(i) + ":  " + str(M[i]).replace("//", "/"))

  m = int(input())
  for _ in range(m):
    n = int(input())
    if n > 256 or n < -60 or M[n] == None:
      print("no solution")
    else:
      print(stringify(*M[n]).replace("//", "/") + " = " + str(n))


if __name__ == "__main__":
  main()