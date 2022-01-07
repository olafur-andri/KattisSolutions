from time import time

def addition(n: int):
  return n + 1

def main():
  SIZE = 1_000_000
  ITERATIONS = 15

  l = list(range(SIZE))

  # `map` mapping
  t_map = 0
  for _ in range(ITERATIONS):
    start_map = time()
    l_map = list(map(addition, l))
    end_mul = time()
    t_map += end_mul - start_map
  print(f"`map`: {round(t_map, 3)}")

  # for mapping
  t_for = 0
  for _ in range(ITERATIONS):
    start_for = time()
    for i in range(len(l)):
      l[i] = addition(l[i])
    end_for = time()
    t_for += end_for - start_for
  print(f"`for`: {round(t_for, 3)}")

if __name__ == "__main__":
  main()