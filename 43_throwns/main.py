from typing import List


def main():
  n, _ = [int(i) for i in input().split()]
  history: List[int] = [0]
  throws_str = input().split()

  curr_kid = 0
  i = 0
  while i < len(throws_str):
    throw_str = throws_str[i]

    if throw_str == "undo":
      nr_undos = int(throws_str[i + 1])
      for _ in range(nr_undos):
        history.pop()
      curr_kid = history[-1]
      i += 1
    
    else:
      throw = int(throw_str)
      curr_kid = (curr_kid + throw) % n
      history.append(curr_kid)
    
    i += 1
  
  print(curr_kid)

if __name__ == "__main__":
  main()