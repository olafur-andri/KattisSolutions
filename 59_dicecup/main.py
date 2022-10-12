def main():
  N, M = tuple(map(int, input().split()))
  start = min(N, M) + 1
  length = abs(M - N) + 1

  for i in range(start, start + length):
    print(i)

if __name__ == "__main__":
  main()