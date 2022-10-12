def main():
  a = int(input())
  b = int(input())
  left = (a - b) % 360
  right = (b - a) % 360
  if left < right:
    print(-left)
  else:
    print(right)

if __name__ == "__main__":
  main()