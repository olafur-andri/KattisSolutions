from collections import deque

def main():
  h, w, _ = [int(i) for i in input().split()]
  lengths = deque([int(i) for i in input().split()])
  rows_finished = 0

  while rows_finished < h:
    cols_finished = 0
    while cols_finished != w:
      if len(lengths) == 0:
        print("NO")
        return
      l = lengths.popleft()
      cols_finished += l
    rows_finished += 1
  
  print("YES")

if __name__ == "__main__":
  main()