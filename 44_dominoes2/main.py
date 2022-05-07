from typing import List, Set


TAL = List[Set[int]]

# returns the amount of dominos knocked over
def knock_over(domino: int, al: TAL, knocked_over: List[bool]):
  count = 0
  queue: List[int] = [domino]
  while len(queue) > 0:
    curr_domino = queue.pop()
    if knocked_over[curr_domino]:
      continue
    count += 1
    knocked_over[curr_domino] = True
    for neighbor in al[curr_domino]:
      queue.append(neighbor)
  return count

def do_test_case():
  n, m, l = [int(i) for i in input().split()]
  knocked_over = [False] * (n + 1)
  al: TAL = [set() for _ in range(n + 1)]
  count = 0

  # read in edges
  for _ in range(m):
    u, v = [int(i) for i in input().split()]
    al[u].add(v)
  
  # time to knock over some Dominoes, baby
  for _ in range(l):
    domino = int(input())
    count += knock_over(domino, al, knocked_over)
  
  print(count)

def main():
  T = int(input())
  for _ in range(T):
    do_test_case()

if __name__ == "__main__":
  main()