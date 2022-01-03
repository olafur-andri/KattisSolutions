from typing import List


def main():
  input()
  tiles: List[int] = [int(i) for i in input().split()]

  # sorting the tiles yields the optimal sequence
  tiles.sort()

  # calculate score
  score = 0
  for i in range(len(tiles) - 1):
    score += (tiles[i] - tiles[i + 1]) ** 2
  print(score)

if __name__ == "__main__":
  main()