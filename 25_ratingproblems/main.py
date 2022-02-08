def main():
  s = 0
  nr_judges, nr_rated = tuple(map(int, input().split()))
  nr_left = nr_judges - nr_rated

  for _ in range(nr_rated):
    s += int(input())
  
  a = nr_left * 3
  min_s = s - a
  max_s = s + a
  print(min_s/nr_judges, max_s/nr_judges)

if __name__ == "__main__":
  main()