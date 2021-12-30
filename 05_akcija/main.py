# I suspect this is a greedy problem. You want to arrange the books such as the
# 3 most expensive books are in the same group, then the next 3 most expensive
# books are in the same group, and so on.
#
# This maximizes the discount, or in other words, minimizes the total cost.

from typing import List


def main():
  # read in all costs
  N = int(input())
  costs: List[int] = []
  worst_total_cost = 0
  for _ in range(N):
    C_i = int(input())
    costs.append(C_i)
    worst_total_cost += C_i
  
  # sort list according to prices in ascending order
  costs.sort()

  # maximize the discount
  max_discount = 0
  for i in range(N - 3, -1, -3):
    max_discount += costs[i]
  
  print(worst_total_cost - max_discount)

if __name__ == "__main__":
  main()