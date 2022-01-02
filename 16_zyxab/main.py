from typing import List

def distinct(name: str):
  s = set(name)
  return len(s) == len(name)

def long_enough(name: str):
  return len(name) >= 5

def main():
  n = int(input())
  names: List[str] = []

  # read in names
  for _ in range(n):
    name = input()
    if distinct(name) and long_enough(name): # first check
      # only collect the shortest names
      if len(names) == 0 or len(names[0]) > len(name):
        names.clear()
        names.append(name)
      elif len(names) > 0 and len(names[0]) == len(name):
        names.append(name)
  
  if len(names) > 0:
    print(max(names))
  else:
    print("neibb!")

if __name__ == "__main__":
  main()