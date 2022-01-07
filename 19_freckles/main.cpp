#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>

/**
 * NOTE: The reason for why I wrote this solution in C++ is exactly the same for
 *       why I decided to solve 'islandhopping' in C++ as well. I have tried to
 *       submit an analogous Python 3 solution to this problem and it always
 *       yields a "Time Limit Exceeded", but the moment the judge sees a C++
 *       solution, it all of a sudden decides to speed up.
 */

struct edge {
  int u, v;
  double w;
};

int root(int i, int* parent) {
  int j = i;

  while (j != parent[j]) {
    parent[j] = parent[parent[j]]; // path compression (cache)
    j = parent[j];
  }

  return j;
}

bool find(int p, int q, int* parent) {
  return root(p, parent) == root(q, parent);
}

void join(int p, int q, int* parent, int* size) {
  int i = root(p, parent);
  int j = root(q, parent);

  if (i == j) { return; }

  if (size[i] < size[j]) {
    parent[i] = j;
    size[j] += size[i];
  } else {
    parent[j] = i;
    size[i] += size[j];
  }
}

double dist(int i, int j, double* xs, double* ys) {
  double dx = xs[i] - xs[j];
  double dy = ys[i] - ys[j];
  return sqrt((dx * dx) + (dy * dy));
}

int comparator(const void* a, const void* b) {
  double val = ((struct edge*)a)->w - ((struct edge*)b)->w;
  return val < 0 ? -1 : (val > 0 ? 1: 0);
}

void do_test_case() {
  int n;
  std::cin >> n;

  int nr_edges = (n * (n-1)) >> 1;

  int* parent = new int[n];
  for (int i = 0; i < n; i += 1) { parent[i] = i; }

  int* size = new int[n];
  for (int i = 0; i < n; i += 1) { size[i] = 1; }
  
  double* xs = new double[n];
  double* ys = new double[n];

  // collect coordinates
  for (int i = 0; i < n; i += 1) {
    double x, y;
    std::cin >> x;
    std::cin >> y;
    xs[i] = x;
    ys[i] = y;
  }
  
  // compute a list of all edges in the fully connected graph
  int index = 0;
  struct edge edges[nr_edges];
  for (int i = 0; i < n; i += 1) {
    for (int j = i + 1; j < n; j += 1) {
      edges[index].u = i;
      edges[index].v = j;
      edges[index].w = dist(i, j, xs, ys);
      index += 1;
    }
  }


  // Kruskal's algorithm for MST
  int mst_count = 0;
  double mst_weight = 0;
  int threshold = n - 1;
  qsort(edges, (size_t)nr_edges, sizeof(struct edge), comparator);
  for (int i = 0; i < nr_edges; i += 1) {
    if (mst_count >= threshold) { break; }
    if (find(edges[i].u, edges[i].v, parent)) { // discard if cycle is created
      continue;
    }

    join(edges[i].u, edges[i].v, parent, size);
    mst_weight += edges[i].w;
    mst_count += 1;
  }
  
  std::cout << std::fixed;
  std::cout << std::setprecision(2);
  std::cout << mst_weight << "\n";

  delete[] parent;
  delete[] size;
  delete[] xs;
  delete[] ys;
}

int main() {
  int T;
  std::cin >> T;

  for (int i = 0; i < T; i += 1) {
    do_test_case();
    
    if (i < T - 1) {
      std::cout << "\n";
    }
  }

  return 0;
}