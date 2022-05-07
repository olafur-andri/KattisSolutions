def main():
  input() # ignore first line
  pieces = list(map(int, input().split()))
  pieces.sort(reverse=True)

  alice = 0
  bob = 0
  for i in range(len(pieces)):
    if i % 2 == 0:
      alice += pieces[i]
    else:
      bob += pieces[i]
  
  print(alice, bob)

if __name__ == "__main__":
  main()