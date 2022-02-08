from typing import Dict
from sys import stdin

def op(i1: int, o: str, i2: int):
  if o == "+": return i1 + i2
  else:        return i1 - i2

def main():
  var_to_val: Dict[str, int] = {}
  val_to_var: Dict[int, str] = {}

  for line in stdin:
    line = line.strip()
    words = line.split()

    if words[0] == "def": # def command
      var = words[1]
      val = int(words[2])
      var_to_val[var] = val
      val_to_var[val] = var
    
    elif words[0] == "calc": # calc command
      s = var_to_val.get(words[1], float("nan"))
      for i in range(3, len(words), 2):
        i2 = var_to_val.get(words[i], float("nan"))
        s = op(s, words[i-1], i2)
      prefix = line[5::]
      res = val_to_var.get(s, "unknown")
      print(f"{prefix} {res}")
    
    elif words[0] == "clear": # clear command
      var_to_val.clear()
      val_to_var.clear()

if __name__ == "__main__":
  main()