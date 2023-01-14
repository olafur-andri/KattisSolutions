def main():
  input()

  # nr_papers[i] designates how many papers of size i+2 we have
  nr_papers = tuple(map(int, input().split()))

  # sidelengths[i] designates how much tape we need to put to papers of size i+2
  # together to create a new paper of size i+1
  sidelengths = [0] * 29
  for i in range(len(sidelengths)):
    power = (-3/4) - (0.5 * i)
    sidelengths[i] = 2 ** power
  
  # the goal is to get sidelengths[0] = 2
  

  print("something")


if __name__ == "__main__":
  main()