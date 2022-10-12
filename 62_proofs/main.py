from typing import Set


def main():
  n = int(input())
  conclusions: Set[str] = set()

  for line_nr in range(n):
    line = input().strip()
    if line.startswith("->"): # line is an axiom
      conclusions.add(line.replace("-> ", ""))
    else:
      assumption_line, conclusion = line.split(" -> ")
      assumptions = assumption_line.split()
      for assumption in assumptions: # check if assumptions are conclusions from prev. lines
        if assumption not in conclusions:
          print(line_nr + 1)
          return
      conclusions.add(conclusion)
  
  print("correct")

if __name__ == "__main__":
  main()