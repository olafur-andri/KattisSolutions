from operator import itemgetter
from typing import Dict, List

TOTAL_TIME = 0
LAP_COUNT = 1

def parse_lap_time(lap_time: str):
  mm, ss = [int(i) for i in lap_time.split(".")]
  return (mm * 60) + ss

def main():
  l, k, s = [int(i) for i in input().split()]
  player_info: Dict[int, List[int, int]] = {}
  finished_players = []

  for _ in range(l):
    split_line = input().split()
    player_id = int(split_line[0])
    player_seconds = parse_lap_time(split_line[1])

    if player_id not in player_info:
      player_info[player_id] = [0, 0]

    # total_times[player_id] += player_seconds
    # lap_counts[player_id] += 1
    player_info[player_id][TOTAL_TIME] += player_seconds
    player_info[player_id][LAP_COUNT] += 1

    if player_info[player_id][LAP_COUNT] == k:
      finished_players.append((player_id, player_info[player_id][TOTAL_TIME]))
  
  finished_players.sort(key=itemgetter(0))
  finished_players.sort(key=itemgetter(1))
  for player in finished_players:
    print(player[0])

if __name__ == "__main__":
  main()