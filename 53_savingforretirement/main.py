from math import ceil

def main():
  Stefan_age, Stefan_r, Stefan_s, Louise_age, Louise_s = \
    [int(i) for i in input().split()]
  Stefan_savings = (Stefan_r - Stefan_age) * Stefan_s
  Louise_nr_years = ceil(Stefan_savings / Louise_s)
  Louise_savings = Louise_s * Louise_nr_years
  if Louise_savings <= Stefan_savings:
    Louise_nr_years += 1
  print(Louise_age + Louise_nr_years)

if __name__ == "__main__":
  main()