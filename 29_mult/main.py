def main():
  n = int(input())
  numbers = [int(input()) for _ in range(n)]
  initial_number = numbers[0]

  i = 1
  while i < len(numbers):
    curr_number = numbers[i]
    if curr_number % initial_number == 0:
      print(curr_number)
      if i < len(numbers) - 1:
        initial_number = numbers[i + 1]
        i += 1
    i += 1

if __name__ == "__main__":
  main()