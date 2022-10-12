from math import sqrt
from typing import List, Tuple


def main():
  c, e, m = tuple(map(int, input().split()))

  if c != 4:
    print("impossible")
    return
  
  # use quadratic formula to obtain roots of 'w'
  A = -1
  B = (e/2) + 4
  C = -e - 4 - m
  w_1 = 0
  w_2 = 0

  try:
    w_1 = ( -B + sqrt(B**2 - 4*A*C) ) / (2*A)
  except ValueError:
    pass

  try:
    w_2 = ( -B - sqrt(B**2 - 4*A*C) ) / (2*A)
  except ValueError:
    pass
  
  w_1 = round(w_1)
  w_2 = round(w_2)
  h_1 = round(e/2 + 4 - w_1)
  h_2 = round(e/2 + 4 - w_2)

  dimensions: List[Tuple[int, int]] = []
  if w_1 >= 2 and h_1 >= 2 and h_1 <= w_1:
    dimensions.append((w_1, h_1))
  if w_2 >= 2 and h_2 >= 2 and h_2 <= w_2:
    dimensions.append((w_2, h_2))
  
  for w, h in dimensions:
    b1 = 2 * (w-2) + 2 * (h-2) + 4 == e + c
    b2 = w * h == e + c + m
    if b1 and b2:
      print(w, h)
      return
  print("impossible")

if __name__ == "__main__":
  main()