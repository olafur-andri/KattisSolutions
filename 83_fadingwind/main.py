def main():
  h, k, v, s = map(int, input().split())
  distance = 0

  while h > 0:
    # step 1
    v += s
    v -= max(1, v // 10)

    # step 2
    if v >= k:
      h += 1
    
    # step 3
    if v > 0 and k > v:
      h -= 1
      if h == 0:
        v = 0

    # step 4
    if v <= 0:
      v = 0
      h = 0

    distance += v

    if s > 0:
      s -= 1

  print(distance)

if __name__ == "__main__":
  main()