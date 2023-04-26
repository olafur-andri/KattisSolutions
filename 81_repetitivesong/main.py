from typing import Dict, List

def find_min_dist(positions: List[int]):
  min_dist = float("inf")
  for i in range(len(positions) - 1):
    curr_dist = positions[i+1] - positions[i]
    min_dist = min(min_dist, curr_dist)
  return min_dist

def main():
  n = int(input())

  # read in words
  words = [""] * n
  for i in range(n):
    words[i] = input()

  # for each word, collect which positions the word appears in in the song
  positions_dict: Dict[str, List[int]] = {}
  for position, word in enumerate(words):
    if word not in positions_dict:
      positions_dict[word] = []
    positions_dict[word].append(position)
  
  # find the minimum distance between copies
  min_dist = n
  for positions in positions_dict.values():
    curr_min_dist = find_min_dist(positions)
    min_dist = min(min_dist, curr_min_dist)
  
  print(n - min_dist)

if __name__ == "__main__":
  main()
