def main():
  n = int(input())
  balance = 0
  min_balance = 0

  for _ in range(n):
    balance += int(input())
    min_balance = min(min_balance, balance)
  
  if min_balance < 0:
    print(-min_balance)
  else:
    print(0)

if __name__ == "__main__":
  main()