def main():
  input() # skip first line
  widths = list(map(int, input().split()))
  counter = 1
  for i in range(1, len(widths)):
    curr_width = widths[i]
    prev_width = widths[i - 1]
    if curr_width > prev_width:
      counter += 1
  print(counter)

if __name__ == "__main__":
  main()