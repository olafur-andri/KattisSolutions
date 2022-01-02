from typing import Dict


def do_test_case(n: int, test_nr: int):
  count_dict: Dict[str, int] = {}
  for _ in range(n):
    animal_name = input().lower().split()[-1]
    count_dict[animal_name] = count_dict.get(animal_name, 0) + 1
  
  print(f"List {test_nr}:")
  items = sorted(count_dict.items())
  for name, count in items:
    print(f"{name} | {count}")

def main():
  counter = 1
  while True:
    n = int(input())
    if n == 0:
      break
    do_test_case(n, counter)
    counter += 1

if __name__ == "__main__":
  main()