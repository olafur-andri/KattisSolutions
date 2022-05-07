from typing import List

#Too slow - since the possible size of the testcases can go quite high up
#Instead you want to make a binary search tree and add nodes when an index is
# flipped to 1 (and remove when flipped to 0). and then you wanted to look 
# through the tree to find all the ones within the interval
# 👍

def main():
  N, K = [int(i) for i in input().split()]
  memory: List[bool] = [False] * (N + 1)
  total_1s = 0

  for _ in range(K):
    tokens = input().split()

    if tokens[0] == "F":
      index = int(tokens[1])
      memory[index] = not memory[index]
      if memory[index]:
        total_1s += 1
      else:
        total_1s -= 1
    
    else:
      f, t = int(tokens[1]), int(tokens[2])
      nr_iterations = (t - f) + 1
      count = 0
      if nr_iterations > (N // 2):
        for i in range(1, f):
          if memory[i]:
            count += 1
        for i in range(t + 1, N + 1):
          if memory[i]:
            count += 1
        count = total_1s - count
      else:
        for i in range(f, t + 1):
          if memory[i]:
            count += 1
      print(count)

if __name__ == "__main__":
  main()