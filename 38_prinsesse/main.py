def linear_search(lo: int, hi: int):
  for i in range(lo, hi + 1):
    print(f"? {i}")
    if input() == "1":
      return i

def main():
  princess_bruised = False
  M, N, S = [int(i) for i in input().split()]

  # commence binary search
  lo = 0
  hi = M - 1

  while lo < hi:
    mid = (lo + hi) // 2
    if N >= M:
      lo = linear_search(lo, hi)
      break
    if S > 0:
      mid = max(lo, mid - 1) # change strategy

    # request princess to sleep
    if princess_bruised:
      N -= S
    req = "? " + " ".join(list(map(str, range(lo, mid + 1))))
    print(req, flush=True)
    N -= 1

    # parse result
    if input() == "1":
      hi = mid
      princess_bruised = True
    else:
      lo = mid + 1
      princess_bruised = False
  
  print(f"! {lo}")

if __name__ == "__main__":
  main()