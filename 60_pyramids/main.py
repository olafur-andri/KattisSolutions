def main():
  N = int(input())
  curr_sidelength = 1
  nr_levels = 0
  nr_blocks = 0

  while nr_blocks <= N:
    nr_blocks += (curr_sidelength ** 2)
    nr_levels += 1
    curr_sidelength += 2
  
  print(nr_levels - 1)

if __name__ == "__main__":
  main()