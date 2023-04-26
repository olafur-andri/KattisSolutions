def main():
  X, Y, N = map(int, input().split())

  for i in range(1, N+1):
    msg = ""
    msg += "Fizz" if i % X == 0 else ""
    msg += "Buzz" if i % Y == 0 else ""
    print(i if msg == "" else msg)

if __name__ == "__main__":
  main()