from operator import itemgetter
from typing import List

def main():
  n = int(input())
  first_times = [None] * n
  other_times = [None] * n

  # read in athletes
  for i in range(n):
    name, first_str, other_str = input().split()
    first_times[i] = (float(first_str), name)
    other_times[i] = (float(other_str), name)
  
  # sort the `other_times` for fast athlete lookup
  other_times.sort(key=itemgetter(0))

  # find the best team (brute force, babbbyyyy)
  best_time = float("inf")
  best_assignment = []

  for first_tuple in first_times:
    first_time, name = first_tuple
    current_time = first_time
    current_assignment: List[str] = [name]

    for second_tuple in other_times:
      if len(current_assignment) >= 4:
        break
      other_time, other_name = second_tuple
      if name == other_name:
        continue
      current_time += other_time
      current_assignment.append(other_name)
    
    if current_time < best_time:
      best_time = current_time
      best_assignment = current_assignment
  
  # print the results
  print(best_time)
  for name in best_assignment:
    print(name)

if __name__ == "__main__":
  main()