import math

def solve(n: int):
  if n == 0: return 0
  return math.ceil(math.log2(n)) + 1

def main():
  n = int(input())
  print(solve(n))

if __name__ == "__main__":
  main()