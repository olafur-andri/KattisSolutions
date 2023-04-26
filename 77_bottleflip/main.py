from math import sqrt

def main():
  h, r, d_a, d_w = map(int, input().split())

  # try first root
  try:
    l_1 = (sqrt(d_a) * h) / (sqrt(d_a) + sqrt(d_w))
    if l_1 > 0 and l_1 < h:
      print(l_1)
      return
  except (ZeroDivisionError, ValueError):
    pass # just try the next root

  # try the second root (no try-except because this has to work)
  l_2 = (sqrt(d_a) * h) / (sqrt(d_a) - sqrt(d_w))
  print(l_2)

if __name__ == "__main__":
  main()
