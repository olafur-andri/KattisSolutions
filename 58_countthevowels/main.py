VOWELS = {'a', 'e', 'i', 'o', 'u'}

def is_vowel(s: str):
  return s in VOWELS
def main():
  s = input().lower()
  i = 0
  for c in s:
    i += int(is_vowel(c))
  print(i)

if __name__ == "__main__":
  main()