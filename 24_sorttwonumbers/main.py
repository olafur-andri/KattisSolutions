def main():
  a, b = tuple(map(int, input().split()))
  print(min(a,b), max(a,b))

if __name__ == "__main__":
  main()