def main():
  pin_1 = input()
  pin_2 = input()
  nr_options = 1
  for d1, d2 in zip(pin_1, pin_2):
    if d1 != d2:
      nr_options *= 2
  print(nr_options)

if __name__ == "__main__":
  main()