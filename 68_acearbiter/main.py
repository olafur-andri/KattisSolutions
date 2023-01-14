def points_are_valid(curr_a: int, curr_b: int, prev_a: int, prev_b: int):
  # game can never result in win for both players
  if curr_a == 11 and curr_b == 11:
    return False
  
  # points may not decrease
  if curr_a < prev_a or curr_b < prev_b:
    return False
  
  # if a player has already won, then the loser's points cannot change
  if curr_a == 11 and prev_a == 11:
    return curr_b == prev_b
  if curr_b == 11 and prev_b == 11:
    return curr_a == prev_a
  
  # everything checks out
  return True


def main():
  n = int(input())

  # collect the rounds *after* which, Alice serves
  alice_rounds = set([0])
  for i in range(3, 50, 4):
    alice_rounds.add(i)
    alice_rounds.add(i+1)

  prev_a, prev_b = -1, -1

  for i in range(n):
    x, y = map(int, input().split("-"))
    round_nr = x + y
    alice_serves = round_nr in alice_rounds

    # learn how many points Alice and Bob have currently
    curr_a, curr_b = (x,y) if alice_serves else (y,x)
    if prev_a == -1:
      prev_a, prev_b = curr_a, curr_b
    
    # check if the current state is valid
    if not points_are_valid(curr_a, curr_b, prev_a, prev_b):
      print(f"error {i+1}")
      return
    
    prev_a, prev_b = curr_a, curr_b
  
  print("ok")

if __name__ == "__main__":
  main()