def main():
  n, q = map(int, input().split())

  cursor = 0
  labels = dict()
  for _ in range(n):
    street_name = input()
    labels[street_name] = cursor
    cursor += 1
  
  for _ in range(q):
    start_name, end_name = input().split()
    start_label = labels[start_name]
    end_label = labels[end_name]
    print(abs(end_label - start_label) - 1)

if __name__ == "__main__":
  main()
