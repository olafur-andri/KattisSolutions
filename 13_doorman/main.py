############
# CONSTANTS
############
MAN = "M"
WOMAN = "W"
EQUAL = "E"


##########
# CLASSES
##########
class WMRatio:
  def __init__(self):
    self.__ratio = 0
  
  def add(self, c: str):
    if c == MAN: self.add_man()
    elif c == WOMAN: self.add_woman()
    else: raise Exception(f"Unrecognized token: '{c}'")
  
  def add_man(self):
    self.__ratio += 1
  
  def add_woman(self):
    self.__ratio -= 1
  
  def equilibrium(self):
    if self.__ratio == 0:  sign = EQUAL
    elif self.__ratio > 0: sign = MAN
    else:                  sign = WOMAN
    return sign, abs(self.__ratio)


class Queue:
  def __init__(self, queue_str: str):
    self.__qs = queue_str
    self.__first = 0
    self.__second = 1
    self.__nr_popped = 0
  
  def peek_first(self):
    return self.__qs[self.__first]
  
  def pop_first(self):
    popped = self.__qs[self.__first]
    self.__first = self.__second
    self.__second += 1
    self.__nr_popped += 1
    return popped
  
  def pop_second(self):
    popped = self.__qs[self.__second]
    self.__second += 1
    self.__nr_popped += 1
    return popped
  
  def first_exists(self):
    return self.__first < len(self.__qs)
  
  def second_exists(self):
    return self.__second < len(self.__qs)
  
  def get_nr_popped(self):
    return self.__nr_popped



###############
# MAIN PROGRAM
###############
# - If W/M ratio is in equilibrium, then pick the first person in line
# - If ratio is not equal, then pick the first person in line only if that
#   person helps restoring the ratio. Otherwise, pick the second person.
def main():
  X = int(input())
  Q = Queue(input())
  R = WMRatio()

  while True:
    alignment, extent = R.equilibrium()

    if extent > X:
      break
    
    if alignment == EQUAL or (Q.first_exists() and Q.peek_first() != alignment):
      if Q.first_exists():
        R.add(Q.pop_first())
      else:
        break
    elif Q.second_exists(): # picking front guest won't help, pick second
      R.add(Q.pop_second())
    else: # want to pick second but there's only one guest left in queue
      if not Q.first_exists() or (extent == X and Q.peek_first() == alignment):
        # either the queue is empty or if we let this person in, Bruno loses
        # track of his counting
        break
      else:
        R.add(Q.pop_first())
        break
  
  # it could be that we popped too many out of the queue, must check
  _, extent = R.equilibrium()
  excess = max(0, extent - X)
  print(Q.get_nr_popped() - excess)

if __name__ == "__main__":
  main()