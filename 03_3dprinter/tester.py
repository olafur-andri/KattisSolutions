from main import solve
from brute import solve_brute

def main():
  for n in range(1, 10_001):
    ans_math = solve(n)
    ans_brute = solve_brute(n)
    if ans_math != ans_brute:
      print("DIFFERENCE FOUND")
      print("n:    ", n)
      print("math: ", ans_math)
      print("brute:", ans_brute)
      return

if __name__ == "__main__":
  main()