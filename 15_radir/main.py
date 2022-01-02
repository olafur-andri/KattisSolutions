from typing import List, Set


def main():
  cardsets: List[Set[int]] = [set() for _ in range(4)]
  n, p = [int(i) for i in input().split()]

  for turn_count in range(1, n + 1):
    suit_id, rank = [int(i) for i in input().split()]
    suit_id -= 1
    cardset = cardsets[suit_id]
    cardset.add(rank)
    low_seq_exists = (rank + 1) in cardset and (rank + 2) in cardset
    mid_seq_exists = (rank - 1) in cardset and (rank + 1) in cardset
    hi_seq_exists  = (rank - 2) in cardset and (rank - 1) in cardset
    if low_seq_exists or mid_seq_exists or hi_seq_exists: # we have a sequence
      print(max(1, turn_count - p))
      return
  
  print("neibb")

if __name__ == "__main__":
  main()