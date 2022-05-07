def main():
  drawing = input()

  # count nr. of left pipes
  nr_left_pipes = 0
  for i in range(0, len(drawing)):
    if drawing[i] == "(":
      break
    nr_left_pipes += 1

  # count nr. of right pipes
  nr_right_pipes = 0
  for i in range(len(drawing) - 1, -1, -1):
    if drawing[i] == ")":
      break
    nr_right_pipes += 1
  
  print("correct" if nr_left_pipes == nr_right_pipes else "fix")

if __name__ == "__main__":
  main()