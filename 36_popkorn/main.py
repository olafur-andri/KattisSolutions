import math

def combinations(n: int):
  return (n * (n - 1)) // 2

def main():
  n = int(input())
  group_size = n // 4
  group_comb = combinations(group_size)
  print((group_comb * 4) + 4)

if __name__ == "__main__":
  main()