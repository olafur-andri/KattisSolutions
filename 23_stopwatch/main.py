from sys import stdin
from typing import List

def main():
  n = int(input())
  ts: List[int] = [-1] * n

  # the stopwatch is still running if n is odd
  if n % 2 == 1:
    print("still running")
    return

  # collect all times
  for i, line in enumerate(stdin):
    ts[i] = int(line)

  # calculate the answer
  answer = 0
  for i in range(1, n, 2):  
    answer += ts[i] - ts[i-1]
  
  print(answer)

if __name__ == "__main__":
  main()