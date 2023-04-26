def main():
  # where does the FizzBuzz sequence start and end?
  start, end = map(int, input().split())

  # read in the Fizzbuzz sequence
  shifted_sequence = input().split()
  sequence = [""] * (end+1)
  for i, e in enumerate(shifted_sequence):
    sequence[start+i] = e

  # our first, really naïve guess is that a, b are super big (if neither "Fizz"
  # nor "Buzz" are mentioned in the sequence)
  a = 100_003
  b = 100_005

  # find first instance of "Fizz..." and update naïve guess
  # use `in` to search to handle "FizzBuzz" case
  for i in range(start, end+1):
    if "Fizz" in sequence[i]:
      a = i
      break
  
  # find second instance of "Fizz..." and lock on concrete value for `a`
  for i in range(a+1, end+1):
    if "Fizz" in sequence[i]:
      a = i - a
      break
  
  # find first instance of "...Buzz" and update naïve guess
  for i in range(start, end+1):
    if "Buzz" in sequence[i]:
      b = i
      break
  
  # find second instance of "...Buzz" and lock on concrete value for `b`
  for i in range(b+1, end+1):
    if "Buzz" in sequence[i]:
      b = i - b
      break
  
  print(a, b)

if __name__ == "__main__":
  main()
