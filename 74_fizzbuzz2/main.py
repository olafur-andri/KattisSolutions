# GLOBAL VARIABLES
TRUTH = []

def correct(i):
  """Returns the correct entry in FizzBuzz sequence for the given number"""
  msg = ""
  msg += "fizz" if i % 3 == 0 else ""
  msg += "buzz" if i % 5 == 0 else ""
  return str(i) if msg == "" else msg

def calculate_score(entries):
  score = 0
  for i, e in enumerate(entries):
    score += int(e == correct(i+1))
  return score

def main():
  N, _ = map(int, input().split())

  # handle output from each candidate
  max_score = 0
  max_candidate = 1
  for i in range(1, N+1):
    curr_entries = input().split()
    curr_score = calculate_score(curr_entries)
    if curr_score > max_score:
      max_score = curr_score
      max_candidate = i
  print(max_candidate)

if __name__ == "__main__":
  main()