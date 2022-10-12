from typing import List, Tuple


TPos = Tuple[int, int]
X = 0
Y = 1
DEPTH_LIMIT = 2

def manhattan(p1: TPos, p2: TPos):
  return abs(p2[X] - p1[X]) + abs(p2[Y] - p1[Y])

def heuristic(p1: TPos, p2: TPos, ai: TPos):
  # remember that the heuristic returns completely 0 whenever the AI piece is
  # caught by one of your pieces
  if p1 == ai or p2 == ai:
    return 0
  return manhattan(p1, ai) + manhattan(p1, ai)

def read_ai_pos() -> TPos:
  """Reads from standard input the position of the AI's piece and stores it in `p`"""
  ai_x, ai_y = tuple(map(int, input("AI: ").split()))
  return (ai_x, ai_y)

def get_possible_moves(n: int, p: TPos):
  moves: List[TPos] = []
  if p[X] > 1: moves.append((p[X] - 1, p[Y])) # go west
  if p[X] < n: moves.append((p[X] + 1, p[Y])) # go east
  if p[Y] > 1: moves.append((p[X], p[Y] - 1)) # go north
  if p[Y] < n: moves.append((p[X], p[Y] + 1)) # go south
  return moves

def min_max_score(n: int, p1: TPos, p2: TPos, ai: TPos, depth: int):
  if depth >= DEPTH_LIMIT:
    return heuristic(p1, p2, ai)
  p1_moves, p2_moves, ai_moves = [p1], [p2], [ai]
  is_my_move = depth % 2 == 0
  if is_my_move:
    p1_moves, p2_moves = get_possible_moves(n, p1), get_possible_moves(n, p2)
  else:
    ai_moves = get_possible_moves(n, ai)
  best_score = heuristic(p1, p2, ai)
  for p1_move in p1_moves:
    for p2_move in p2_moves:
      for ai_move in ai_moves:
        new_score = min_max_score(n, p1_move, p2_move, ai_move, depth + 1)
        best_score = min(new_score, best_score) if is_my_move else max(new_score, best_score)
  return best_score

def min_max_root(n: int, p1: TPos, p2: TPos, ai: TPos):
  p1_moves = get_possible_moves(n, p1)
  p2_moves = get_possible_moves(n, p2)
  # NOTE: If doing alpha-beta pruning, may want to order the moves such that the first moves bring you closer to the AI
  min_score = heuristic(p1, p2, ai) # heuristic of making no move
  best_p1_move = p1
  best_p2_move = p2
  for p1_move in p1_moves:
    for p2_move in p2_moves:
      score = min_max_score(n, p1_move, p2_move, ai, 1)
      if score < min_score:
        min_score = score
        best_p1_move = p1
        best_p2_move = p2
  return best_p1_move, best_p2_move

def print_board(n: int, p1: TPos, p2: TPos, ai: TPos):
  s = ""
  for y in range(1, n + 1):
    for x in range(1, n + 1):
      curr = (x, y)
      if curr == p1:
        s += "1"
      elif curr == p2:
        s += "2"
      elif curr == ai:
        s += "A"
      else:
        s += "."
      s += " "
    s += "\n"
  print(s)

def main():
  n = int(input())
  x_1, y_1, x_2, y_2 = tuple(map(int, input().split()))
  p1 = (x_1, y_1)
  p2 = (x_2, y_2)
  ai = read_ai_pos()

  print_board(n, p1, p2, ai)
  # input()
  
  game_over = False
  while not game_over:
    p1, p2 = min_max_root(n, p1, p2, ai)
    # print(f"{p1[X]} {p1[Y]} {p2[X]} {p2[Y]}")
    print_board(n, p1, p2, ai)
    ai = read_ai_pos()
    game_over = p1 == ai or p2 == ai
    

if __name__ == "__main__":
  main()