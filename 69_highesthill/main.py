def main():
  n = int(input())
  H = tuple(map(int, input().split()))

  # pre-compute left-slump of all heights
  L = list(range(n)) # L[i] = index of the left slump for index i
  # L[0] = 0 holds automatically
  for i in range(1, n):
    if H[i] >= H[i-1]:
      L[i] = L[i-1]
  
  # pre-compute right-slump of all heights
  R = list(range(n)) # R[i] = index of the right slump for index i
  # R[n-1] = n-1 holds automatically
  for i in range(n-2, -1, -1):
    if H[i] >= H[i+1]:
      R[i] = R[i+1]

  # use pre-computed values L[...] & R[...] to try all possible peaks
  tallest_peak = 0
  for i in range(n):
    curr_peak = min(H[i] - H[L[i]], H[i] - H[R[i]])
    tallest_peak = max(tallest_peak, curr_peak)
  print(tallest_peak)


if __name__ == "__main__":
  main()