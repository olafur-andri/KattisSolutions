from typing import List

M: List[str] = []

def op(i1: int, i2: int, o: str):
  if o == "*": return i1 * i2
  if o == "+": return i1 + i2
  if o == "-": return i1 - i2
  if o == "/": return i1 // i2
  raise ValueError(f"Unexpected operation: '{o}'")

def op_valid(i1: int, i2: int, o: str):
  return i2 != 0 or o != "/"

def pretty_print(a: int, b: int, c: int, d: int, ops: str):
  print(f"{a} {ops[0]} {b} = {c} {ops[1]} {d}")

def build_M(a: int, b: int, c: int, d: int, acc: str = ""):
  if len(acc) == 2:
    if op_valid(a, b, acc[0]) and \
       op_valid(c, d, acc[1]) and \
       op(a, b, acc[0]) == op(c, d, acc[1]):
      M.append(acc)
    return
  
  build_M(a, b, c, d, acc + "*")
  build_M(a, b, c, d, acc + "+")
  build_M(a, b, c, d, acc + "-")
  build_M(a, b, c, d, acc + "/")

def main():
  a, b, c, d = [int(i) for i in input().split()]
  build_M(a, b, c, d)

  if len(M) == 0:
    print("problems ahead")
  else:
    for ops in M:
      pretty_print(a, b, c, d, ops)

if __name__ == "__main__":
  main()