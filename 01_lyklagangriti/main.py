from typing import List


LEFT = "L"
RIGHT = "R"
BACK = "B"

def decode(s: str):
  password: List[str] = []
  cursor = 0

  for c in s:
    if c == LEFT:
      cursor -= 1
    elif c == RIGHT:
      cursor += 1
    elif c == BACK:
      del password[cursor - 1]
      cursor -= 1
    else:
      password.insert(cursor, c)
      cursor += 1
  
  return "".join(password)

def main():
  s = input()
  print(decode(s))

if __name__ == "__main__":
  main()