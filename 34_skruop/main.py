UP = "Skru op!"

def main():
  level = 7
  n = int(input())
  for _ in range(n):
    request = input()
    if request == UP:
      level = min(10, level + 1)
    else:
      level = max(0, level - 1)
  print(level)

if __name__ == "__main__":
  main()