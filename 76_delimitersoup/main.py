from string import whitespace

# GLOBALS
OPENING_DELIM = { "(", "[", "{" } # all opening delimiters
CLOSING_DELIM = { "(": ")", "[": "]", "{": "}" } # corresponding closing delimiters

def main():
  # don't need to know the length of the next line
  input()

  # read in the program line
  line = input().strip()

  # go through each character and maintain a stack of delimiters
  delim_stack = []
  for i, c in enumerate(line):
    if c in whitespace: # ignore whitespace
      continue
    if c in OPENING_DELIM:
      delim_stack.append(c)
    elif len(delim_stack) == 0 or c != CLOSING_DELIM[delim_stack.pop()]:
      print(c, i)
      return
  
  # ok so far
  print("ok so far")


if __name__ == "__main__":
  main()
