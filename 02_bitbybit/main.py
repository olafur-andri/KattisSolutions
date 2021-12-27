from typing import List, Set

TRegister = List[Set[bool]]

def create_register():
  """ Create the initial values for the register. Every bit could be either
      1 or 0. Most significant bit on the left.
  """
  return [set([False, True]) for _ in range(32)]

def bit_pos_to_reg_index(bit_pos: int):
  return 31 - bit_pos

def bitwise_and(register: TRegister, index_i: int, index_j: int):
  possible_outcomes = set()
  for i_val in register[index_i]:
    for j_val in register[index_j]:
      possible_outcomes.add(i_val and j_val)
  return possible_outcomes

def bitwise_or(register: TRegister, index_i: int, index_j: int):
  possible_outcomes = set()
  for i_val in register[index_i]:
    for j_val in register[index_j]:
      possible_outcomes.add(i_val or j_val)
  return possible_outcomes

def perform_op(op: str, register: TRegister):
  split_op = op.strip().split()
  op_type = split_op[0]
  if op_type == "SET":
    bit_pos = int(split_op[1])
    reg_index = bit_pos_to_reg_index(bit_pos)
    register[reg_index] = set([True])
  elif op_type == "CLEAR":
    bit_pos = int(split_op[1])
    reg_index = bit_pos_to_reg_index(bit_pos)
    register[reg_index] = set([False])
  elif op_type == "AND":
    bit_pos_i, bit_pos_j = int(split_op[1]), int(split_op[2])
    reg_index_i = bit_pos_to_reg_index(bit_pos_i)
    reg_index_j = bit_pos_to_reg_index(bit_pos_j)
    register[reg_index_i] = bitwise_and(register, reg_index_i, reg_index_j)
  elif op_type == "OR":
    bit_pos_i, bit_pos_j = int(split_op[1]), int(split_op[2])
    reg_index_i = bit_pos_to_reg_index(bit_pos_i)
    reg_index_j = bit_pos_to_reg_index(bit_pos_j)
    register[reg_index_i] = bitwise_or(register, reg_index_i, reg_index_j)

def print_register(register: TRegister):
  line = ""
  for s in register:
    if len(s) == 2: line += "?"
    elif True in s: line += "1"
    else:           line += "0"
  print(line)

def main():
  while True:
    n = int(input())
    if n == 0:
      return
    
    register = create_register()
    for _ in range(n):
      perform_op(input(), register)
    
    print_register(register)

if __name__ == "__main__":
  main()