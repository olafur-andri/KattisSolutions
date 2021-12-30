from typing import List


OPS = ["+", "-", "*", "/"]
ALPHABET = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0",
]

def parse_line():
  ab, c = input().split(" = ")
  a, b, op = "", "", ""
  for curr_op in OPS:
    if curr_op in ab:
      a, b = ab.split(f" {curr_op} ")
      op = curr_op
      break
  return a, b, c, op

def from_unary(s: str):
  res = 0
  for c in s:
    if c == "1":
      res += 1
    else:
      raise ValueError(f"invalid literal '{s}' for unary base")
  return res

def perform_op(a: int, b: int, op: str):
  if op == "+":
    return a + b
  if op == "-":
    return a - b
  if op == "*":
    return a * b
  if op == "/":
    return a / b
  raise ValueError(f"invalid operation: '{op}'")

def get_base_name(base: int):
  if base >= 1 and base <= 9:
    return str(base)
  return ALPHABET[base - 10]

def to_int(s: str, source_base: int):
  if source_base == 1: # special case for unary base
    return from_unary(s)
  return int(s, source_base)

def main():
  N = int(input())
  for _ in range(N):
    valid_bases: List[bool] = [False] * 37
    a, b, c, op = parse_line()

    # check for all bases
    for curr_base in range(1, 37):
      try:
        int_a = to_int(a, curr_base)
        int_b = to_int(b, curr_base)
        int_c = to_int(c, curr_base)
        if perform_op(int_a, int_b, op) == int_c:
          valid_bases[curr_base] = True
      except ValueError:
        pass
    
    # construct output string
    answer = ""
    for curr_base in range(1, 37):
      if not valid_bases[curr_base]:
        continue
      answer += get_base_name(curr_base)
    
    if answer != "":
      print(answer)
    else:
      print("invalid")

if __name__ == "__main__":
  main()