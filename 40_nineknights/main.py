from typing import List, Set, Tuple

HEIGHT = 5
WIDTH = 5
TCoord = Tuple[int, int]

def add(c1: TCoord, c2: TCoord):
  return (c1[0] + c2[0], c2[1] + c1[1])

def get_all_moves(coord: TCoord):
  # collect all moves, even the impossible ones
  moves: List[TCoord] = []
  for horizontal_jump in range(1, 3):
    vertical_jump = 3 - horizontal_jump
    moves.append(add(coord, (-horizontal_jump, vertical_jump)))
    moves.append(add(coord, (-horizontal_jump, -vertical_jump)))
    moves.append(add(coord, (horizontal_jump, vertical_jump)))
    moves.append(add(coord, (horizontal_jump, -vertical_jump)))
  return moves

def main():
  bad_coords: Set[TCoord] = set()

  # collect all bad coordinates
  for row_id in range(WIDTH):
    row = input()
    for col_id, c in enumerate(row):
      if c == "k":
        bad_coords.add((row_id, col_id))
  
  # make sure we have 9 knights (thanks, Sara)
  if len(bad_coords) != 9:
    print("invalid")
    return
  
  for knight_coord in bad_coords:
    possible_coords = get_all_moves(knight_coord)
    for coord in possible_coords:
      if coord in bad_coords:
        print("invalid")
        return
  
  print("valid")

if __name__ == "__main__":
  main()