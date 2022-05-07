import math

def main():
  L, R = [int(i) for i in input().split()]
  l = L / 2
  min_radius = math.sqrt((l**2) + (l**2))
  print("nope" if R < min_radius else "fits")

if __name__ == "__main__":
  main()