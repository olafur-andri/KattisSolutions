code_array = [ord(elem) for elem in input()]

print(chr(sum(code_array) // len(code_array)))