from typing import Tuple


TPos = Tuple[int, int]
X = 0
Y = 1

def sign(i: int):
  if i > 0: return 1
  if i < 0: return -1
  return 0

def p1_move(p: TPos, ai: TPos) -> TPos: # horizontal-first
  x_move = sign(ai[X] - p[X])
  if x_move != 0:
    return (p[X] + x_move, p[Y])
  y_move = sign(ai[Y] - p[Y])
  return (p[X], p[Y] + y_move)

def p2_move(p: TPos, ai: TPos) -> TPos: # vertical-first
  y_move = sign(ai[Y] - p[Y])
  if y_move != 0:
    return (p[X], p[Y] + y_move)
  x_move = sign(ai[X] - p[X])
  return (p[X] + x_move, p[Y])

def main():
  _ = int(input())
  x_1, y_1, x_2, y_2 = tuple(map(int, input().split()))
  p1 = (x_1, y_1)
  p2 = (x_2, y_2)
  ai = tuple(map(int, input().split()))
  
  game_over = False
  while not game_over:
    p1 = p1_move(p1, ai)
    p2 = p2_move(p2, ai)
    print(f"{p1[X]} {p1[Y]} {p2[X]} {p2[Y]}")
    ai = tuple(map(int, input().split()))
    game_over = ai[X] == 0 and ai[Y] == 0

if __name__ == "__main__":
  main()