def main():
  a,b = [int(elem) for elem in input().split()]
  if a > b:
    print(1)
  else:
    print(0)

if __name__ == "__main__":
  main()