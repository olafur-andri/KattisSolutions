from typing import List, Tuple


TRange = Tuple[int, int]

def print_range(r: TRange):
  a, b = r
  if a == b:
    print(a, end="")
  else:
    print(f"{a}-{b}", end="")

def main():
  nr_lines, _ = tuple(map(int, input().split()))
  error_lines = list(map(int, input().split()))
  errors: List[TRange] = []
  corrects: List[TRange] = []

  # add all preliminary correct lines
  if error_lines[0] > 1:
    corrects.append((1, error_lines[0] - 1))

  i = 0
  while i < len(error_lines):
    # try to build a range for errors
    j = i
    while j < len(error_lines) - 1 and error_lines[j] == error_lines[j + 1] - 1:
      j += 1
    errors.append((error_lines[i], error_lines[j]))
    i = j + 1

    # add correct lines to `corrects`
    try:
      corrects.append((error_lines[j] + 1, error_lines[i] - 1))
    except Exception:
      pass
  
  # add all correct lines at the end of the file
  if error_lines[-1] < nr_lines:
    corrects.append((error_lines[-1] + 1, nr_lines))
  
  # print the results
  print("Errors: ", end="")
  for i, correct in enumerate(errors):
    print_range(correct)
    if i < len(errors) - 2:
      print(", ", end="")
    elif i == len(errors) - 2:
      print(" and ", end="")
  
  print("\nCorrect: ", end="")
  for i, correct in enumerate(corrects):
    print_range(correct)
    if i < len(corrects) - 2:
      print(", ", end="")
    elif i == len(corrects) - 2:
      print(" and ", end="")

if __name__ == "__main__":
  main()