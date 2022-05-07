from typing import Set, Tuple


BITMASK = ""
COSTS: Tuple[int] = []
MASK_BAG: Set[str] = set()
MIN_COST: int = float("inf")

def flip_bit(bit: str):
  return "0" if bit == "1" else "1"

# i: starting index, cost: the current accumulated cost
def solve(i: int, cost: int):
  """Find the min. cost to build a bitmask for characters i, i+1, ..., n"""
  global MIN_COST
  if i == len(BITMASK):
    MIN_COST = min(MIN_COST, cost)
    return

  max_mask_len = len(BITMASK) - i
  for mask_len in range(1, max_mask_len + 1):
    mask = BITMASK[i:i+mask_len] # try to build the next `mask_len` mask bits
    mask_already_made = mask in MASK_BAG
    if not mask_already_made:
      MASK_BAG.add(mask)

    mask_cost = 0 if mask_already_made else COSTS[mask_len]
    solve(i + mask_len, cost + mask_cost)

    if not mask_already_made:
      MASK_BAG.remove(mask)


def main():
  global BITMASK
  global COSTS
  BITMASK = "".join(map(flip_bit, input()))
  COSTS = (0,) + tuple(map(int, input().split())) # shifted to account for 1-indexing
  solve(0, 0)
  print(MIN_COST)


if __name__ == "__main__":
  main()