n, x, y = [int(elem) for elem in input().split()]

multiplier = y / x

for _ in range(n):
  ingredient = int(input())
  print(round(ingredient * multiplier))
