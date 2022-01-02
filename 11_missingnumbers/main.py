def main():
  n = int(input())
  expected_num = 1
  gap_found = False
  for _ in range(n):
    given_num = int(input())
    if given_num > expected_num:
      gap_found = True
      for i in range(expected_num, given_num): # print missing numbers
        print(i)
    expected_num = given_num + 1
  if not gap_found:
    print("good job")

if __name__ == "__main__":
  main()