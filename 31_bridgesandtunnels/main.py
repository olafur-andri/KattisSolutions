from typing import Dict, List, Set, Tuple


TBridge = Tuple[int, int]


##############
# DEPENDENCIES
##############
# shamelessly stolen from https://gist.github.com/artkpv/6f0591c01a940d6ebe1344a8efa88847
# changed a bit for clarity's sake and added some extra documentation to help
# me understand what the hell is going on in the code for future reference

class UnionFind:
  """Weighted quick-union with path compression and connected components.
  The original Java implementation is introduced at
  https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
  >>> uf = UnionFind(10)
  >>> for (p, q) in [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9),
  ...                (7, 3), (4, 8), (6, 1)]:
  ...     uf.union(p, q)
  >>> uf._id
  [8, 3, 3, 3, 3, 3, 3, 3, 3, 3]
  >>> uf.find(0, 1)
  True
  >>> uf._id
  [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
  """

  __slots__ = ["_size", "_parent", "_depth", "cc"]

  def __init__(self, n: int):
    self._parent = list(range(n))
    self._size = [1] * n
    self.cc = n  # nr. of connected components

  def root(self, i: int):
    """Returns the ID of the root of the i-th node (w/ path compression)"""
    j = i
    while j != self._parent[j]:
      self._parent[j] = self._parent[self._parent[j]] # path compression (cache)
      j = self._parent[j]
    return j

  def find(self, p: int, q: int):
    """Returns True iff p-th and q-th node have the same parent"""
    return self.root(p) == self.root(q)

  def union(self, p: int, q: int):
    """Connect p-th and q-th nodes' roots together"""
    i = self.root(p)
    j = self.root(q)
    if i == j:
      return
    if self._size[i] < self._size[j]:
      self._parent[i] = j
      self._size[j] += self._size[i]
    else:
      self._parent[j] = i
      self._size[i] += self._size[j]
    self.cc -= 1
  
  def size(self, p: int):
    """Get the number of p's children + 1"""
    return self._size[p]


##############
# MAIN PROGRAM
##############
def main():
  n = int(input())

  # collect all bridges & count nr. of distinct buildings
  buildings: Dict[str, int] = {}
  bridges: List[TBridge] = [None] * n
  for i in range(n):
    b1, b2 = input().split()
    if b1 not in buildings:
      buildings[b1] = len(buildings)
    if b2 not in buildings:
      buildings[b2] = len(buildings)
    bridges[i] = (buildings[b1], buildings[b2])
  
  # go through each bridge
  uf = UnionFind(len(buildings))
  for bridge in bridges:
    b1, b2 = bridge
    uf.union(b1, b2)
    print(uf.size(uf.root(b1)))

if __name__ == "__main__":
  main()