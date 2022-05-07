def main():
  greeting = input()
  nr_es = len(greeting) - 2
  es = "e" * (nr_es * 2)
  response = f"h{es}y"
  print(response)

if __name__ == "__main__":
  main()