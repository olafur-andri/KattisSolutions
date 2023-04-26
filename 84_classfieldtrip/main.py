from typing import List

def main():
  counts: List[int] = [0] * ( ord("z") + 1 )
  
  a = input()
  b = input()

  for c in a:
    counts[ord(c)] += 1
  for c in b:
    counts[ord(c)] += 1
  
  for i in range(ord("a"), ord("z")+1):
    print(chr(i) * counts[i], end="")
  print()


if __name__ == "__main__":
  main()
