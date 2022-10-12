from collections import deque
from typing import Deque

# one possible solution is to use a dequeue for fast insertion and removal of
# characters

def main():
  line = input()

  q: Deque[str] = deque()
  for c in line:
    if c == "<":
      try:
        q.pop()
      except:
        pass
    else:
      q.append(c)
  
  print("".join(q))

if __name__ == "__main__":
  main()