def x_or_o_won(state: str, bit: str):
  # all vertical, horizontal, and diagonal wins
  return (state[-10] == state[-13] == state[-16] == bit and (state[-1] == state[-4] == state[-7] == "1")) or \
         (state[-11] == state[-14] == state[-17] == bit and (state[-2] == state[-5] == state[-8] == "1")) or \
         (state[-12] == state[-15] == state[-18] == bit and (state[-3] == state[-6] == state[-9] == "1")) or \
        \
        (state[-10] == state[-11] == state[-12] == bit and (state[-1] == state[-2] == state[-3] == "1")) or \
        (state[-13] == state[-14] == state[-15] == bit and (state[-4] == state[-5] == state[-6] == "1")) or \
        (state[-16] == state[-17] == state[-18] == bit and (state[-7] == state[-8] == state[-9] == "1")) or \
        \
        (state[-10] == state[-14] == state[-18] == bit and (state[-1] == state[-5] == state[-9] == "1")) or \
        (state[-12] == state[-14] == state[-16] == bit and (state[-3] == state[-5] == state[-7] == "1"))

def x_won(state: str):
  return x_or_o_won(state, "1")

def o_won(state: str):
  return x_or_o_won(state, "0")

def every_tile_played(state: str):
  return state.endswith("111111111")

def tic_tac_do():
  # gather binary representation of board state
  num = int(input()[1::], 8)
  board_state = format(num, "b")
  l = len(board_state)
  board_state = ("0" * (19 - l)) + board_state

  if x_won(board_state):
    print("X wins")
  elif o_won(board_state):
    print("O wins")
  elif every_tile_played(board_state):
    print("Cat's")
  else:
    print("In progress")


def main():
  c = int(input())
  for _ in range(c):
    tic_tac_do()

if __name__ == "__main__":
  main()