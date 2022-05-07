from typing import List


GROUND = "."
MONEY = "$"
GEM = "*"
INCENSE = "|"
TRADER = "t"
JEWELER = "j"
BANKER = "b"

def go_on_an_adventure():
  backpack: List[str] = []
  adventure = input()
  for c in adventure:
    if c == GROUND:
      continue
    elif c == BANKER:
      if len(backpack) == 0:
        return False
      elif backpack.pop() != MONEY:
        return False
    elif c == JEWELER:
      if len(backpack) == 0:
        return False
      elif backpack.pop() != GEM:
        return False
    elif c == TRADER:
      if len(backpack) == 0:
        return False
      elif backpack.pop() != INCENSE:
        return False
    else:
      backpack.append(c) # add item to backpack
  return len(backpack) == 0

def main():
  n = int(input())
  for _ in range(n):
    print("YES" if go_on_an_adventure() else "NO")

if __name__ == "__main__":
  main()