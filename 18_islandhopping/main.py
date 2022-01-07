# NOTE: THIS PYTHON FILE WILL NOT BE ACCEPTED BY KATTIS, IT IS TOO SLOW.
#       Even though I'm solving this problem exactly the way I'm doing it in
#       the C++ file, it doesn't solve it in time, sadly. This file does a good
#       job, however, at describing how I'm solving it for non-C++ programmers.
#       So that'll do.

from math import hypot
from typing import List, Tuple
from operator import itemgetter

########
# TYPES
########
TCoord = Tuple[float, float]
TEdge = Tuple[float, int, int] # length, endpoint 1, endpoint 2

###############
# MAIN PROGRAM
###############
def root(i: int, parent: List[int]):
  """Returns the ID of the root of the i-th node (w/ path compression)"""
  j = i
  while j != parent[j]:
    parent[j] = parent[parent[j]] # path compression (cache)
    j = parent[j]
  return j

def find(p: int, q: int, parent: List[int]):
  """Returns True iff p-th and q-th node have the same parent"""
  return root(p, parent) == root(q, parent)

def union(p: int, q: int, parent: List[int], size: List[int]):
  """Connect p-th and q-th nodes' roots together"""
  i = root(p, parent)
  j = root(q, parent)
  if i == j:
    return
  if size[i] < size[j]:
    parent[i] = j
    size[j] += size[i]
  else:
    parent[j] = i
    size[i] += size[j]

def dist(i: int, j: int, xs: List[int], ys: List[int]):
  dx = xs[i] - xs[j]
  dy = ys[i] - ys[j]
  return hypot(dx, dy)

def do_test_case():
  m = int(input())
  nr_edges = (m * (m-1)) >> 1
  parent = list(range(m))
  size = [1] * m
  xs: List[int] = [0] * m
  ys: List[int] = [0] * m

  # collect coordinates
  for i in range(m):
    xs[i], ys[i] = list(map(float, input().split()))
  
  # compute a list of all edges in the fully connected graph
  index = 0
  edges: List[TEdge] = [0] * nr_edges
  for i in range(m):
    for j in range(i + 1, m):
      edges[index] = (dist(i, j, xs, ys), i, j)
      index += 1


  # Kruskal's algorithm for MST
  mst_count = 0
  mst_weight = 0
  threshold = m - 1
  edges.sort(key=itemgetter(0)) # sort edges by their weight (descending because stack)
  for i in range(nr_edges):
    if mst_count >= threshold:
      break
    if find(edges[i][1], edges[i][2], parent): # discard if cycle is created
      continue
    union(edges[i][1], edges[i][2], parent, size)
    mst_weight += edges[i][0]
    mst_count += 1
  
  print(mst_weight)

def main():
  n = int(input())
  for _ in range(n):
    do_test_case()

if __name__ == "__main__":
  main()