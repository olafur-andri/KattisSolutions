from typing import Dict


def main():
  _, Q = map(int, input().split())
  capital: Dict[int, int] = {}
  otherwise: int = 0

  for _ in range(Q):
    tokens = input().split()
    if tokens[0] == "SET":
      i, x = int(tokens[1]), int(tokens[2])
      capital[i] = x
    elif tokens[0] == "RESTART":
      capital.clear()
      x = int(tokens[1])
      otherwise = x
    else: # "PRINT"
      i = int(tokens[1])
      print(capital.get(i, otherwise))

if __name__ == "__main__":
  main()