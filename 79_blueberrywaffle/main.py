def main():
  r, f = map(int, input().split())
  total_degrees_rotated = 180 * (f / r)
  rotation = total_degrees_rotated % 360
  if rotation > 90.0 and rotation < 270:
    print("down")
  else:
    print("up")

if __name__ == "__main__":
  main()
