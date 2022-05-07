COEFFICIENTS = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

def main():
  cpr = input().replace("-", "")
  digits = [int(c) for c in cpr]
  summer = 0
  for i in range(len(digits)):
    summer += digits[i] * COEFFICIENTS[i]
  print(int(summer % 11 == 0))

if __name__ == "__main__":
  main()