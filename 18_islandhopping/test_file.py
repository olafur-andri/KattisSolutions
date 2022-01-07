from io import TextIOWrapper
import random


def write_test_case(fs: TextIOWrapper):
  m = 750
  fs.write(f"{m}\n")
  for _ in range(m):
    x, y = random.uniform(-1_000, 1_000), random.uniform(-1_000, 1_000)
    x, y = round(x, 3), round(y, 3)
    fs.write(f"{x} {y}\n")

def main():
  n = 10
  with open("0.in", "w") as fs:
    fs.write(f"{n}\n")
    for _ in range(n):
      write_test_case(fs)

if __name__ == "__main__":
  main()