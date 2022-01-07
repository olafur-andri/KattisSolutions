# Kruskal's algorithm for finding a MST
from typing import List, Tuple
from operator import itemgetter
from UnionFind import UnionFind

TEdge = Tuple[float, int, int] # weight, endpoint 1, endpoint 2

def kruskal(n: int, edges: List[TEdge]):
  mst_count = 0
  mst_weight = 0
  threshold = n - 1
  nr_edges = len(edges)
  uf = UnionFind(n)
  edges.sort(key=itemgetter(0)) # sort edges by their weight (descending because stack)
  for i in range(nr_edges): # `for` loop faster than `while`
    if mst_count >= threshold:
      break
    if uf.find(edges[i][1], edges[i][2]): # discard if cycle is created
      continue
    uf.union(edges[i][1], edges[i][2])
    mst_weight += edges[i][0]
    mst_count += 1