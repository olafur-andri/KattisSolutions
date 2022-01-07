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

  __slots__ = ["_parent", "_depth", "cc"]

  def __init__(self, n: int):
    self._parent = list(range(n))
    self._size = [1] * n
    self.cc = n  # nr. of connected components

  def _root(self, i: int):
    """Returns the ID of the root of the i-th node (w/ path compression)"""
    j = i
    while j != self._parent[j]:
      self._parent[j] = self._parent[self._parent[j]] # path compression (cache)
      j = self._parent[j]
    return j

  def find(self, p: int, q: int):
    """Returns True iff p-th and q-th node have the same parent"""
    return self._root(p) == self._root(q)

  def union(self, p: int, q: int):
    """Connect p-th and q-th nodes' roots together"""
    i = self._root(p)
    j = self._root(q)
    if i == j:
      return
    if self._size[i] < self._size[j]:
      self._parent[i] = j
      self._size[j] += self._size[i]
    else:
      self._parent[j] = i
      self._size[i] += self._size[j]
    self.cc -= 1