def main():
  G, T, _ = [int(i) for i in input().split()]
  item_weight = sum(map(int, input().split()))
  actual = int((G - T) * 0.9)
  print(actual - item_weight)

if __name__ == "__main__":
  main()