def is_moon_time(curr_year: int, year_moon: int, interval_moon: int):
  return (curr_year + year_moon) % interval_moon == 0

def main():
  year_sun, interval_sun = map(int, input().split())
  year_moon, interval_moon = map(int, input().split())

  curr_year = interval_sun - year_sun

  while curr_year <= 5_000:
    if is_moon_time(curr_year, year_moon, interval_moon):
      print(curr_year)
      break
    curr_year += interval_sun

if __name__ == "__main__":
  main()
