import statistics

def main():
  C = int(input())
  for _ in range(C):
    grades = [int(i) for i in input().split()][1::] # discard `N`
    mean = statistics.mean(grades)

    # count how many grades exceed the mean
    nr_above = 0
    for g in grades:
      if g > mean:
        nr_above += 1
    
    answer = (nr_above / len(grades)) * 100
    print(f"{round(answer, 3):.3f}" + "%")

if __name__ == "__main__":
  main()