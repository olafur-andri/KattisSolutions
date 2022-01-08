from typing import Dict


def main():
  n = int(input())
  xs = list(map(int, input().split()))

  min_dist = n
  last_index: Dict[int, int] = {}
  for i, x in enumerate(xs):
    if x in last_index:
      min_dist = min(i - last_index[x], min_dist)
    last_index[x] = i
  
  print(min_dist)

if __name__ == "__main__":
  main()