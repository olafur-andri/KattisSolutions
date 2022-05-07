from typing import List, Set, Tuple


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

TTile = Tuple[int, int]

def turn_left(direction: int):
  return (direction - 1) % 4

def turn_right(direction: int):
  return (direction + 1) % 4

def u_turn(direction: int):
  return (direction + 2) % 4

def walk_forward(position: TTile, direction: int):
  x, y = position
  if direction == NORTH:
    return (x, y + 1)
  if direction == EAST:
    return (x + 1, y)
  if direction == SOUTH:
    return (x, y - 1)
  if direction == WEST:
    return (x - 1, y)

def main():
  location = (0, 0)
  direction = NORTH
  tiles: Set[TTile] = { (0, 0) }

  # read instructions
  input()
  instructions = input().split()

  # execute instructions and build maze
  for instruction in instructions:
    if instruction == "<":
      direction = turn_left(direction)
    elif instruction == ">":
      direction = turn_right(direction)
    elif instruction == "U":
      direction = u_turn(direction)
    else:
      nr_steps = int(instruction)
      for _ in range(nr_steps):
        location = walk_forward(location, direction)
        tiles.add(location)

if __name__ == "__main__":
  main()