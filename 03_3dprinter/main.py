import math

# fastest way to print `n` statues is simply to double the printers every day
# until you've reached or surpassed `n`. Then you simply need one day to print
# the remaining statues.

def solve(n: int):
  if n == 0: return 0
  return math.ceil(math.log2(n)) + 1

def main():
  n = int(input())
  print(solve(n))

if __name__ == "__main__":
  main()